from storage import load_faqs
from faq import show_faqs, find_faq, add_faq, delete_faq

faqs = []

def main():
    while True:
        print("===AI Customer Support Platform===")
        print('1. Add FAQ.')
        print('2. Show all FAQs.')
        print('3. Find FAQ.')
        print('4. Delete FAQ.')
        print('5. Exit.')

        choice = input('Choose option: ')

        if choice == '1':
            print()
            print('===Post this question in the FAQ.===')
            add_faq(faqs)
        elif choice == '2':
            print()
            print('===All FAQs:===')
            show_faqs(faqs)
        elif choice == '3':
            print()
            print('===Results for your query:===')
            find_faq(faqs)
        elif choice == '4':
            print('===Delete FAQ===')
            delete_faq(faqs)
        elif choice == '5':
            print('Bye!')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == "__main__":
    faqs = load_faqs()
    main()
