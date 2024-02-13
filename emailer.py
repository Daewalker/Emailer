def generate_email_template():  # Get user inputs
    
    team_name = input("Enter the team to email: ")
    device_alarming = input("Enter the device alarming: ")
    alarm_description = input("Enter the alarm: ")

    # Email template
    email_subject = f"Alarm Notification: {device_alarming} - {alarm_description}"
    email_body = f"Hello {team_name},\n\n" \
                 f"We have device: [{device_alarming}] alarming with the following details:\n" \
                 f"Alarm: '{alarm_description}'\n\n" \
                 "Please take necessary actions to address the issue.\n\n" \
                 "Regards,\nJamie Valentonis\nHughes NMC\n Phone: +1 (301) 601-4205 Option 1"

    return email_subject, email_body

def main():
    # Generate email template
    subject, body = generate_email_template()

    # Display the email template
    print("\nGenerated Email Template:")
    print("Subject:", subject)
    print("\nBody:")
    print(body)

if __name__ == "__main__":
    main()
