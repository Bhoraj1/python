import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Check if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number."
        
        # Get country/region description
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Get carrier name
        carrier_name = carrier.name_for_number(parsed_number, "en")
        
        return f"Location: {location}\nCarrier: {carrier_name}"
    except phonenumbers.NumberParseException:
        return "Error parsing phone number."

if __name__ == "__main__":
    phone = input("Enter your phone number (with country code, e.g., +14155552671): ")
    info = get_phone_info(phone)
    print(info)
