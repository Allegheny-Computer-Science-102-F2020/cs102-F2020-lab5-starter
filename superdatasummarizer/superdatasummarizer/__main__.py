"""Define the command-line interface for the superdatasummarizer program."""

# TODO: import the Path object from the pathlib class


# TODO: import the typer package


# TODO: import the summarize and transform modules
# from the superdatasummarizer package


def main(
    data_file: Path = typer.Option(...),
):
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        typer.echo("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        typer.echo("")
        typer.echo(f"The data file contains {data_line_count} data values in it!")
        typer.echo("Let's do some SUPER summarizing! 🚀")
        # transform the data from a list of textual values to a list of numerical values
        data_list = transform.transform_string_to_number_list(data_text)
        # compute the mean from the list of numerical values
        computed_mean = summarize.compute_mean(data_list)
        # display the computed mean in the terminal window
        typer.echo("")
        typer.echo(f"The computed mean is {computed_mean}!")
        # TODO: compute the median from the list of numerical values
        # TODO: display the computed median in the terminal window
        # compute the variance from the list of numerical values
        computed_variance = summarize.compute_variance(data_list)
        # display the computed variance in the terminal window
        typer.echo(f"The computed variance is {computed_variance}!")
        # TODO: compute the standard deviation from the list of numerical values
        # TODO: display the computed standard deviation in the terminal window
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not data_file.exists():
        typer.echo("The data file does not exist!")


if __name__ == "__main__":
    # indirectly call the main function through the typer.run function
    typer.run(main)
