"""Generate a dated Pages post or email a published Horizon digest."""

import argparse
import os
import subprocess
import sys
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from src.models import EmailConfig
from src.services.email import EmailManager


REPOSITORY = Path(__file__).resolve().parents[1]
DELIVERY_DATE = REPOSITORY / "data" / "pages-last-emailed.txt"


def generate(edition: date, post_path: Path) -> None:
    with TemporaryDirectory(prefix="horizon-") as directory:
        working_dir = Path(directory)
        state_dir = working_dir / "data"
        (working_dir / "profiles").symlink_to(REPOSITORY / "profiles", target_is_directory=True)
        subprocess.run(
            [
                sys.executable, "-m", "src.main",
                "--config", str(REPOSITORY / "data" / "config.pages.json"),
                "--data-dir", str(state_dir),
            ],
            cwd=working_dir,
            env={**os.environ, "PYTHON_DOTENV_DISABLED": "1"},
            check=True,
        )
        summaries = list((state_dir / "summaries").glob("horizon-*-zh.md"))
        if len(summaries) > 1:
            raise RuntimeError("Horizon generated more than one Chinese report")
        body = "过去 24 小时没有收录的条目。"
        if summaries:
            markdown = summaries[0].read_text(encoding="utf-8")
            first_line, _, remainder = markdown.partition("\n")
            body = remainder.strip() if first_line.startswith("# ") else markdown.strip()

    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text(
        f'---\nlayout: default\ntitle: "Horizon 中文日报 · {edition}"\n'
        f"date: {edition}\nlang: zh\ngenerated_by: horizon-pages\n---\n\n{body}\n",
        encoding="utf-8",
    )
    print(f"Prepared a Chinese digest for {edition}")


def send_email(edition: date, post_path: Path) -> None:
    if DELIVERY_DATE.exists() and date.fromisoformat(
        DELIVERY_DATE.read_text(encoding="utf-8").strip()
    ) >= edition:
        print(f"The digest for {edition} was already emailed")
        return

    address = os.environ["QQ_SMTP_EMAIL"]
    site = os.environ["HORIZON_SITE_URL"].rstrip("/")
    edition_url = f"{site}/{edition:%Y/%m/%d}/summary-zh.html"
    _, _, body = post_path.read_text(encoding="utf-8").partition("\n---\n")
    subject = f"Horizon 中文日报 · {edition}"
    summary = f"# {subject}\n\n[在网页阅读本期]({edition_url})\n\n{body.strip()}"
    settings = EmailConfig(
        enabled=True,
        email_address=address,
        password_env="QQ_SMTP_AUTH_CODE",
        sender_name="Horizon 日报",
        smtp_server="smtp.qq.com",
        smtp_port=465,
        imap_server="",
        imap_enabled=False,
    )
    if EmailManager(settings).send_daily_summary(summary, subject, [address]) != 1:
        raise RuntimeError("The SMTP server did not accept the digest")
    DELIVERY_DATE.write_text(f"{edition}\n", encoding="utf-8")
    print(f"QQ SMTP accepted the digest for {edition}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("generate", "email"))
    parser.add_argument("date", type=date.fromisoformat)
    args = parser.parse_args()
    post_path = REPOSITORY / "docs" / "_posts" / f"{args.date}-summary-zh.md"
    action = generate if args.action == "generate" else send_email
    action(args.date, post_path)


if __name__ == "__main__":
    main()
