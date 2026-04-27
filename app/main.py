def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line"),
        "column": error.get("column", 0),
        "code": error.get("code"),
        "message": error.get("message"),
        "source": error.get("source", "flake8")
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    formatted_errors = [format_linter_error(err) for err in errors]
    return {
        "path": file_path,
        "status": "failed" if formatted_errors else "passed",
        "errors": formatted_errors
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
