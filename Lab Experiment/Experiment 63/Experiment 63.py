import csv
from collections import defaultdict


filename = input("Enter process execution log file: ")


# Predefined expected parent-child relationships
expected_parents = {

    "explorer.exe": [
        "winword.exe",
        "excel.exe",
        "notepad.exe",
        "chrome.exe",
        "firefox.exe"
    ],

    "cmd.exe": [
        "powershell.exe"
    ],

    "powershell.exe": [
        "python.exe",
        "script.exe"
    ],

    "services.exe": [
        "svchost.exe"
    ]
}


processes = []
children = defaultdict(list)


try:

    with open(filename, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            process = {
                "pid": row["PID"],
                "process_name": row["ProcessName"],
                "parent_pid": row["ParentPID"],
                "parent_name": row["ParentProcess"]
            }

            processes.append(process)

            children[
                row["ParentPID"]
            ].append(process)


    print("\nPROCESS HIERARCHY ANALYSIS")
    print("========================================")


    print("\nPROCESS EXECUTION RECORDS")
    print("----------------------------------------")

    for process in processes:

        print(
            "\nParent Process:",
            process["parent_name"]
        )

        print(
            "Parent PID:",
            process["parent_pid"]
        )

        print(
            "Child Process:",
            process["process_name"]
        )

        print(
            "Process PID:",
            process["pid"]
        )


    print("\nSUSPICIOUS PARENT-CHILD RELATIONSHIPS")
    print("----------------------------------------")


    suspicious_found = False


    for process in processes:

        parent = process[
            "parent_name"
        ].lower()

        child = process[
            "process_name"
        ].lower()


        if parent in expected_parents:

            if child not in expected_parents[parent]:

                suspicious_found = True

                print(
                    "\n[SUSPICIOUS RELATIONSHIP]"
                )

                print(
                    "Parent Process:",
                    process["parent_name"]
                )

                print(
                    "Parent PID:",
                    process["parent_pid"]
                )

                print(
                    "Child Process:",
                    process["process_name"]
                )

                print(
                    "Child PID:",
                    process["pid"]
                )

                print(
                    "Reason: Child process is not "
                    "listed as an expected process "
                    "for this parent."
                )


    if not suspicious_found:

        print(
            "No suspicious parent-child "
            "relationships detected."
        )


except FileNotFoundError:

    print(
        "Process execution log file does not exist."
    )

except Exception as e:

    print("Error:", e)
