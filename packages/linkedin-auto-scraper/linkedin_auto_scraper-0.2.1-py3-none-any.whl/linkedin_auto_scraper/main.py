from typing import ContextManager, Optional

import typer
from alive_progress import alive_bar
from rich import print

from linkedin_auto_scraper.utils.utils import Scraper, to_console, to_excel

s = Scraper()
app = typer.Typer()
state = {"verbose": False}


def spinner(title: Optional[str] = None) -> ContextManager:
    """
    Context manager to display a spinner while a long-running process is running.

    Usage:
        with spinner("Fetching data..."):
            fetch_data()

    Args:
        title: The title of the spinner. If None, no title will be displayed.
    """
    return alive_bar(monitor=None, stats=None, title=title)


@app.command()
def login():
    """
    login to linkedin acount
    """
    email = typer.prompt("Email")
    password = typer.prompt(
        "Password", hide_input=True, confirmation_prompt=True
    )
    try:
        with spinner("Accessing linkedin with your credentials..."):
            login = s.linkedin_login(email=email, password=password)
        if login == "Login Successful":
            print(
                "you have succesfully login your linkedin account. :fireworks:"
            )
    except Exception as e:
        print(type(e))
        print(
            "[bold red]alert![/bold red] Please check your network connection or credentials validity and try again!"
        )
        s.quit_driver()
    s.quit_driver()


@app.command()
def scrape(
    search: str = typer.Option(
        "hr", "--search", "-s", help="Search parameter."
    ),
    location: str = typer.Option(
        None,
        "--location",
        "-l",
        help="Use it if you want to search a particular location e.g Nigeria",
    ),
    excel: bool = typer.Option(
        ..., prompt="Would you like to save to excel document?"
    ),
):
    """
    Scrape peoples data from the linkedin
    """
    my_list = []
    try:
        with spinner(
            "Accessing linkedin with your credentials and scrapping data..."
        ):
            links = s.scrape_linkedin_job_links(
                search_params=search, country_filter_param=location
            )

            for link in links:
                info = s.scarpe_link_info(link=link)
                if info not in my_list and len(info) > 0:
                    my_list.append(info)
        if excel:
            name = typer.prompt("What would you like to save the file as?")
            sheet_name = typer.prompt("Choose a sheet name.")
            to_excel(data=my_list, file_name=name, sheet_name=sheet_name)
        else:
            print(to_console(data=my_list))
    except Exception as e:
        print(e)
        print(
            "[bold red]alert![/bold red] Please check your network connection and try again!"
        )
        s.quit_driver()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    This Software is created by Emeka Okafor.
    """
    if ctx.invoked_subcommand is None:
        print(
            "[bold yellow]Usage:[/bold yellow] main.py [OPTIONS] COMMAND [ARGS]...\n[light grey]Try[/light grey] 'linkedin-auto-scraper --help' [light grey]for help.[/light grey]"
        )

    if ctx.invoked_subcommand == "login":
        print("\n[bold blue]lets log you in [/bold blue]\n")

    if ctx.invoked_subcommand == "scrape":
        print("\n[bold blue]Starting the scrapping process...[/bold blue]\n")


if __name__ == "__main__":
    app()
