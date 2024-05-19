import argparse
import pyfiglet

def generate_email_addresses(first_name, last_name, domain, format_choice):
    first_name = first_name.lower()
    last_name = last_name.lower()
    first_initial = first_name[0]
    
    if format_choice == 1:
        return f"{first_name}.{last_name}@{domain}"
    elif format_choice == 2:
        return f"{first_name}{last_name}@{domain}"
    elif format_choice == 3:
        return f"{first_initial}.{last_name}@{domain}"
    elif format_choice == 4:
        return f"{first_initial}{last_name}@{domain}"
    elif format_choice == 5:
        return f"{first_name}@{domain}"
    elif format_choice == 6:
        return f"{last_name}@{domain}"
    else:
        raise ValueError("Invalid format choice")

def process_bulk_input(input_file, domain, format_choice, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            first_name, last_name = line.strip().split()
            email_address = generate_email_addresses(first_name, last_name, domain, format_choice)
            outfile.write(f"Generated email address for {first_name} {last_name}: {email_address}\n")

def main():
    title = pyfiglet.figlet_format("Email Generator", font="slant")
    author = pyfiglet.figlet_format("Whitehat94", font="digital")
    
    print(title)
    print(author)

    parser = argparse.ArgumentParser(description="Generate email addresses from a list of names.")
    parser.add_argument("input_file", help="Input file containing names")
    parser.add_argument("domain", help="Domain name for the email addresses")
    parser.add_argument("output_file", help="Output file to save the generated email addresses")
    
    args = parser.parse_args()

    print("Choose an email format:")
    print("1: first.last@domain.com")
    print("2: firstlast@domain.com")
    print("3: f.last@domain.com")
    print("4: flast@domain.com")
    print("5: first@domain.com")
    print("6: last@domain.com")
    
    format_choice = int(input("Enter the number of your chosen format: "))
    
    process_bulk_input(args.input_file, args.domain, format_choice, args.output_file)
    print(f"Email addresses have been written to {args.output_file}")

if __name__ == "__main__":
    main()
