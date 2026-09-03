import os
from datetime import datetime


folder = input("Enter directory path: ")

start_date = input(
    "Enter start date (YYYY-MM-DD): "
)

end_date = input(
    "Enter end date (YYYY-MM-DD): "
)

event_filter = input(
    "Enter event type (Created/Modified/Accessed/All): "
).lower()


try:

    start_time = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    )

    end_time = datetime.strptime(
        end_date,
        "%Y-%m-%d"
    )

    events = []

    for root, directories, files in os.walk(folder):

        for filename in files:

            filepath = os.path.join(
                root,
                filename
            )

            try:

                created = datetime.fromtimestamp(
                    os.path.getctime(filepath)
                )

                modified = datetime.fromtimestamp(
                    os.path.getmtime(filepath)
                )

                accessed = datetime.fromtimestamp(
                    os.path.getatime(filepath)
                )


                file_events = [
                    ("Created", created),
                    ("Modified", modified),
                    ("Accessed", accessed)
                ]


                for event_type, event_time in file_events:

                    if (
                        start_time <= event_time <= end_time
                    ):

                        if (
                            event_filter == "all"
                            or event_filter
                            == event_type.lower()
                        ):

                            events.append(
                                (
                                    event_time,
                                    event_type,
                                    filepath
                                )
                            )

            except FileNotFoundError:
                pass


    events.sort(key=lambda x: x[0])


    print("\nFILE TIMESTAMP ANALYSIS")
    print("================================")

    print(
        "\nDate Range:",
        start_date,
        "to",
        end_date
    )

    print(
        "Event Filter:",
        event_filter.upper()
    )

    print("\nCHRONOLOGICAL RESULTS")
    print("--------------------------------")


    if events:

        for event in events:

            event_time = event[0]
            event_type = event[1]
            filepath = event[2]

            print(
                event_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "|",
                event_type,
                "|",
                filepath
            )

    else:

        print(
            "No matching file events found."
        )


except ValueError:

    print(
        "Invalid date format. "
        "Use YYYY-MM-DD."
    )

except FileNotFoundError:

    print("Directory does not exist.")

except Exception as e:

    print("Error:", e)
