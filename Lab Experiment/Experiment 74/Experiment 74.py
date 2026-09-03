from difflib import SequenceMatcher


# Legitimate organizational domains
legitimate_domains = [
    "google.com",
    "microsoft.com",
    "amazon.com",
    "saveetha.com"
]


# Suspicious-looking domains
suspicious_domains = [
    "go0gle.com",
    "google-login.com",
    "googlle.com",
    "microsoft-security.com",
    "micros0ft.com",
    "amazon-verify.com",
    "saveetha-login.com"
]


def similarity(domain1, domain2):

    return SequenceMatcher(
        None,
        domain1,
        domain2
    ).ratio()


def detect_patterns(
    suspicious,
    legitimate
):

    warnings = []


    # Remove .com for comparison
    suspicious_name = suspicious.replace(
        ".com",
        ""
    )

    legitimate_name = legitimate.replace(
        ".com",
        ""
    )


    # ----------------------------------------
    # Character Substitution
    # ----------------------------------------

    substitutions = {
        "0": "o",
        "1": "l",
        "3": "e",
        "@": "a"
    }


    for suspicious_char, normal_char in (
        substitutions.items()
    ):

        if suspicious_char in suspicious_name:

            possible_name = suspicious_name.replace(
                suspicious_char,
                normal_char
            )

            if legitimate_name in possible_name:

                warnings.append(
                    "Possible character substitution"
                )


    # ----------------------------------------
    # Additional Characters
    # ----------------------------------------

    if (
        legitimate_name in suspicious_name
        and suspicious_name
        != legitimate_name
    ):

        warnings.append(
            "Additional characters detected"
        )


    # ----------------------------------------
    # Hyphenation
    # ----------------------------------------

    if "-" in suspicious_name:

        warnings.append(
            "Hyphenation pattern detected"
        )


    # ----------------------------------------
    # Repeated Characters
    # ----------------------------------------

    for i in range(
        len(suspicious_name) - 1
    ):

        if (
            suspicious_name[i]
            == suspicious_name[i + 1]
        ):

            warnings.append(
                "Repeated character detected"
            )

            break


    # ----------------------------------------
    # Misleading Prefix or Suffix
    # ----------------------------------------

    suspicious_words = [
        "login",
        "verify",
        "security",
        "account",
        "secure"
    ]


    for word in suspicious_words:

        if word in suspicious_name:

            warnings.append(
                "Misleading prefix or suffix: "
                + word
            )


    return warnings


print(
    "\nDOMAIN LOOK-ALIKE ANALYSIS"
)

print(
    "========================================"
)


for suspicious in suspicious_domains:

    best_match = None

    highest_similarity = 0


    # ----------------------------------------
    # Find Closest Legitimate Domain
    # ----------------------------------------

    for legitimate in legitimate_domains:

        score = similarity(
            suspicious,
            legitimate
        )


        if score > highest_similarity:

            highest_similarity = score

            best_match = legitimate


    # ----------------------------------------
    # Detect Suspicious Patterns
    # ----------------------------------------

    warnings = detect_patterns(
        suspicious,
        best_match
    )


    print(
        "\nSUSPICIOUS DOMAIN:",
        suspicious
    )

    print(
        "Closest Legitimate Domain:",
        best_match
    )

    print(
        "Similarity Score:",
        round(
            highest_similarity * 100,
            2
        ),
        "%"
    )


    if warnings:

        print(
            "Detected Patterns:"
        )

        for warning in warnings:

            print(
                "-",
                warning
            )

    else:

        print(
            "No predefined look-alike "
            "pattern detected."
        )
