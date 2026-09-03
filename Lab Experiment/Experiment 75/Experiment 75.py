import whois
from collections import defaultdict


filename = input(
    "Enter domain list file: "
)


results = []


try:

    # ----------------------------------------
    # Read Domain Names
    # ----------------------------------------

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        domains = [
            line.strip()
            for line in file
            if line.strip()
        ]


    print(
        "\nDOMAIN OSINT INVESTIGATION"
    )

    print(
        "========================================"
    )


    # ----------------------------------------
    # Perform WHOIS Lookup
    # ----------------------------------------

    for domain in domains:

        print(
            "\nInvestigating:",
            domain
        )


        try:

            information = whois.whois(
                domain
            )


            registrar = information.registrar


            creation_date = (
                information.creation_date
            )


            expiration_date = (
                information.expiration_date
            )


            name_servers = (
                information.name_servers
            )


            # Handle multiple dates

            if isinstance(
                creation_date,
                list
            ):

                creation_date = creation_date[0]


            if isinstance(
                expiration_date,
                list
            ):

                expiration_date = expiration_date[0]


            # Handle missing name servers

            if not name_servers:

                name_servers = []


            results.append({
                "domain": domain,
                "registrar": registrar,
                "creation_date":
                    creation_date,
                "expiration_date":
                    expiration_date,
                "name_servers":
                    list(name_servers)
                    if name_servers
                    else []
            })


        except Exception as e:

            print(
                "WHOIS lookup failed for",
                domain
            )

            print(
                "Reason:",
                e
            )


    # ----------------------------------------
    # Display Domain Information
    # ----------------------------------------

    print(
        "\nINVESTIGATION RESULTS"
    )

    print(
        "========================================"
    )


    for record in results:

        print(
            "\nDomain:",
            record["domain"]
        )


        print(
            "Registrar:",
            record["registrar"]
        )


        print(
            "Registration Date:",
            record["creation_date"]
        )


        print(
            "Expiration Date:",
            record["expiration_date"]
        )


        print(
            "Name Servers:"
        )


        if record["name_servers"]:

            for server in (
                record["name_servers"]
            ):

                print(
                    "-",
                    server
                )

        else:

            print(
                "Not Available"
            )


    # ----------------------------------------
    # Group by Registrar
    # ----------------------------------------

    registrar_groups = defaultdict(
        list
    )


    for record in results:

        registrar = (
            record["registrar"]
        )


        if registrar:

            registrar_groups[
                registrar
            ].append(
                record["domain"]
            )


    print(
        "\nCOMMON REGISTRATION CHARACTERISTICS"
    )

    print(
        "========================================"
    )


    print(
        "\nDOMAINS SHARING THE SAME REGISTRAR"
    )


    common_registrar_found = False


    for (
        registrar,
        domain_list
    ) in registrar_groups.items():


        if len(domain_list) > 1:

            common_registrar_found = True


            print(
                "\nRegistrar:",
                registrar
            )


            print(
                "Domains:"
            )


            for domain in domain_list:

                print(
                    "-",
                    domain
                )


    if not common_registrar_found:

        print(
            "No multiple domains with the "
            "same registrar were identified."
        )


    # ----------------------------------------
    # Investigation Summary
    # ----------------------------------------

    print(
        "\nINVESTIGATION SUMMARY"
    )

    print(
        "========================================"
    )


    print(
        "Total Domains Investigated:",
        len(domains)
    )


    print(
        "Successful WHOIS Results:",
        len(results)
    )


    print(
        "Failed Investigations:",
        len(domains)
        - len(results)
    )


except FileNotFoundError:

    print(
        "Domain list file does not exist."
    )


except Exception as e:

    print(
        "Error:",
        e
    )
