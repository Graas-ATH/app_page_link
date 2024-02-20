import streamlit as st

def validate_cron_schedule(schedule):
    # Split the schedule string into its components
    components = schedule.split()

    st.write(components)
    # Check if there are exactly 5 components
    if len(components) != 5:
        return False

    # Define the ranges for each cron field
    ranges = [
        (0, 59),  # minutes
        (0, 23),  # hours
        (1, 31),  # day of month
        (1, 12),  # month
        (0, 6)    # day of week (0 = Sunday)
    ]

    for i, (start, end) in enumerate(ranges):
        try:
            value = components[i]
            st.write(value)
            if value != '*' and (int(value) < start or int(value)  > end):
                return False
        except ValueError:
            # If the value is not an integer, it's invalid
            if value != '*':
                return False

    return True

def main():
    st.title("Cron Schedule Validator")

    # Text input for the cron schedule
    schedule = st.text_input("Enter cron schedule:")

    # Validate the schedule when there's a change
    if schedule:
        if validate_cron_schedule(schedule):
            st.success("Valid cron schedule!")
        else:
            st.error("Invalid cron schedule. Please check and try again.")
    
    st.page_link("https://app.snowflake.com/wjldhhw/oi28270/#/streamlit-apps/GP_STG_DWH.PUBLIC.JYSJ8Y37MHMOU9DS", label="app")

if __name__ == "__main__":
    main()
