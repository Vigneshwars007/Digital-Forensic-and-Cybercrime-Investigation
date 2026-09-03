import csv
from datetime import datetime


filename = input(
    "Enter incident record file: "
)


events = []


# Expected incident response phases
phases = [
    "Detection",
    "Investigation",
    "Containment",
    "Eradication",
    "Recovery",
    "Post-Incident Review"
]


try:

    # ----------------------------------------
    # Read Incident Records
    # ----------------------------------------

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)


        for row in reader:

            timestamp = datetime.strptime(
                row["Timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )


            events.append({
                "timestamp": timestamp,
                "phase": row["Phase"],
                "description": row["Description"]
            })


    # ----------------------------------------
    # Sort Events Chronologically
    # ----------------------------------------

    events.sort(
        key=lambda x: x["timestamp"]
    )


    print(
        "\nINCIDENT RESPONSE RECONSTRUCTION"
    )

    print(
        "========================================"
    )


    # ----------------------------------------
    # Display Chronological Timeline
    # ----------------------------------------

    print(
        "\nCHRONOLOGICAL INCIDENT TIMELINE"
    )

    print(
        "----------------------------------------"
    )


    for event in events:

        print(
            event["timestamp"].strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        print(
            "Phase:",
            event["phase"]
        )

        print(
            "Event:",
            event["description"]
        )

        print(
            "----------------------------------------"
        )


    # ----------------------------------------
    # Find First Event of Each Phase
    # ----------------------------------------

    phase_start_times = {}


    for phase in phases:

        phase_events = [
            event
            for event in events
            if event["phase"].lower()
            == phase.lower()
        ]


        if phase_events:

            phase_start_times[
                phase
            ] = phase_events[0][
                "timestamp"
            ]


    # ----------------------------------------
    # Display Phase Summary
    # ----------------------------------------

    print(
        "\nINCIDENT RESPONSE PHASE SUMMARY"
    )

    print(
        "========================================"
    )


    for phase in phases:

        if phase in phase_start_times:

            print(
                phase,
                "started at:",
                phase_start_times[
                    phase
                ].strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )

        else:

            print(
                phase,
                ": No record found"
            )


    # ----------------------------------------
    # Calculate Duration Between Phases
    # ----------------------------------------

    print(
        "\nDURATION BETWEEN MAJOR PHASES"
    )

    print(
        "========================================"
    )


    available_phases = [
        phase
        for phase in phases
        if phase in phase_start_times
    ]


    for i in range(
        len(available_phases) - 1
    ):

        current_phase = (
            available_phases[i]
        )

        next_phase = (
            available_phases[i + 1]
        )


        current_time = (
            phase_start_times[
                current_phase
            ]
        )


        next_time = (
            phase_start_times[
                next_phase
            ]
        )


        duration = (
            next_time
            - current_time
        )


        print(
            current_phase,
            "to",
            next_phase
        )

        print(
            "Duration:",
            duration
        )

        print(
            "----------------------------------------"
        )


    # ----------------------------------------
    # Total Incident Duration
    # ----------------------------------------

    if len(events) > 1:

        total_duration = (
            events[-1]["timestamp"]
            - events[0]["timestamp"]
        )


        print(
            "\nTOTAL INCIDENT RESPONSE DURATION:"
        )

        print(
            total_duration
        )


    # ----------------------------------------
    # Final Summary
    # ----------------------------------------

    print(
        "\nINCIDENT RESPONSE SUMMARY"
    )

    print(
        "========================================"
    )


    print(
        "Total Events:",
        len(events)
    )


    print(
        "Phases Identified:",
        len(available_phases)
    )


    print(
        "First Recorded Event:",
        events[0][
            "timestamp"
        ].strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )


    print(
        "Last Recorded Event:",
        events[-1][
            "timestamp"
        ].strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )


except FileNotFoundError:

    print(
        "Incident record file does not exist."
    )


except ValueError:

    print(
        "Invalid timestamp format."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
