import pandas as pd
import os


def clean_data(df):
    # Drop columns with 100% missing values
    df = df.drop(columns=["UCR_PART", "OFFENSE_CODE_GROUP"])

    return df


def compile_data(data_folder, output_file):
    compiled_df = pd.DataFrame()

    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(data_folder, filename)
            df = pd.read_csv(file_path, low_memory=False)
            print(f"\nProcessing file: {filename}")
            cleaned_df = clean_data(df)
            compiled_df = pd.concat([compiled_df, cleaned_df], ignore_index=True)

    compiled_df.to_csv(output_file, index=False)
    print(f"\nCompiled data saved to {output_file}")


def categorize_crime(row):

    categories = {
        "violent_crimes": [
            "ASSAULT",
            "MURDER",
            "KIDNAPPING",
            "INTIMIDATING WITNESS",
            "NEGLIGENCE",
            "SUICIDE / SUICIDE ATTEMPT",
            "AFFRAY",
            "Justifiable Homicide",
        ],
        "property_crimes": [
            "LARCENY",
            "VANDALISM",
            "BREAKING AND ENTERING",
            "AUTO THEFT",
            "ARSON",
            "BURGLARY",
            "PROPERTY - STOLEN THEN RECOVERED",
            "STOLEN PROPERTY",
            "GRAFFITI",
            "TRESPASSING",
            "ROBBERY",
            "POSSESSION OF BURGLARIOUS TOOLS",
        ],
        "investigation": [
            "DEATH INVESTIGATION",
            "INVESTIGATE PERSON",
            "INVESTIGATE PROPERTY",
            "MISSING PERSON",
            "PROPERTY - LOST/ MISSING",
            "PROPERTY - LOST THEN LOCATED",
            "SEARCH WARRANT",
            "FUGITIVE FROM JUSTICE",
            "BOMB THREAT",
            "AIRCRAFT INCIDENTS",
            "PRISONER ESCAPE / ESCAPE & RECAPTURE",
            "Evidence Tracker Incidents",
        ],
        "disorderly_conduct_harassment": [
            "HARASSMENT",
            "OBSCENE PHONE CALLS",
            "THREATS TO DO BODILY HARM",
            "VERBAL DISPUTE",
            "DISTURBING THE PEACE",
            "DISORDERLY CONDUCT",
            "DRUNKENNESS",
            "LIQUOR/ALCOHOL - DRINKING IN PUBLIC",
            "NOISY PARTY/RADIO-NO ARREST",
            "RESTRAINING ORDER",
        ],
        "public_safety": [
            "SICK",
            "FIRE REPORT",
            "CHILD REQUIRING ASSISTANCE",
            "PROTECTIVE CUSTODY / SAFEKEEPING",
            "DANGEROUS OR HAZARDOUS CONDITION",
            "SUDDEN DEATH",
        ],
        "animal_related": [
            "ANIMAL ABUSE",
            "ANIMAL INCIDENTS",
        ],
        "legal_violations": ["VIOLATION", "WARRANT ARREST"],
        "weapons_crimes": [
            "Weapon",
            "Firearm",
            "Explosives",
            "BALLISTICS EVIDENCE/FOUND",
        ],
        "fraud_crimes": [
            "FRAUD",
            "FORGERY",
            "COUNTERFEITING",
            "EMBEZZLEMENT",
            "EVADING FARE",
            "EXTORTION OR BLACKMAIL",
        ],
        "misc": [
            "LANDLORD - TENANT",
            "OTHER OFFENSE",
            "PRISONER - SUICIDE / SUICIDE ATTEMPT",
            "PROPERTY - ACCIDENTAL DAMAGE",
            "PROPERTY - FOUND",
            "PROSTITUTION",
            "PROSTITUTION - ASSISTING OR PROMOTING",
            "PROSTITUTION - SOLICITING",
            "SERVICE TO OTHER AGENCY",
            "TRUANCY / RUNAWAY",
        ],
        "drug_crimes": ["DRUGS", "DRUG"],
        "traffic_related_crimes": [
            "M/V",
            "VAL",
            "OPERATING UNDER THE INFLUENCE",
            "VEHICLE",
            "MV",
        ],
    }
    for category, keywords in categories.items():
        pattern = "|".join(keywords)
        if (
            pd.notna(row["OFFENSE_DESCRIPTION"])
            and pd.Series(row["OFFENSE_DESCRIPTION"])
            .str.contains(pattern, case=False, na=False)
            .any()
        ):
            return category
    return "Uncategorized"


if __name__ == "__main__":
    data_folder = "data/raw"
    output_file = "data/processed/compiled_data.csv"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # compile_data(data_folder, output_file)
    df = pd.read_csv(output_file, low_memory=False)
    df["CATEGORY"] = df.apply(categorize_crime, axis=1)
    cat_output_file = "data/processed/categorized_data.csv"
    df.to_csv(cat_output_file, index=False)
