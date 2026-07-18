from storage import  save_faqs, load_faqs

faqs = []

def add_faq():
    while True:
        question = input('Enter question: ').strip()
        answer = input('Enter answer: ').strip()

        if question == '' or answer == '':
            print('Question and answer cannot be empty.')
        else:
            faq = {'question': question, 'answer': answer}
            faqs.append(faq)
            print('FAQ added!')
            save_faqs(faqs)
            break

def show_faqs():
    if faqs:
        for i in range(len(faqs)):
            print(f'{i+1}. {faqs[i]["question"]}: \n {faqs[i]["answer"]}')
    else:
        print("No FAQs available")

def find_faq():
    request = input('Enter search request: ').lower().strip()

    if request == '':
        print('Search request cannot be empty.')
        return

    coincidence = []

    for faq in faqs:
        if request in faq['question'].lower():
            coincidence.append(faq)

    if coincidence:
        for i in range(len(coincidence)):
            print(f"{i + 1}. {coincidence[i]['question']}:")
            print(f"   {coincidence[i]['answer']}\n")
    else:
        print('No matching FAQs found.')

def delete_faq():
    if not faqs:
        print('No FAQ available')
    else:
        show_faqs()
        while True:
            try:
                print(f'Enter number from 1 to {len(faqs)}:')
                number = int(input())
                if number <= 0 or number > len(faqs):
                    print('Invalid FAQ number')
                else:
                    deleted_faq = faqs.pop(number-1)
                    save_faqs(faqs)
                    print(f"Deleted:{deleted_faq['question']}")
                    break
            except ValueError:
                print('Please, enter a number.')

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
            add_faq()
        elif choice == '2':
            print()
            print('===All FAQs:===')
            show_faqs()
        elif choice == '3':
            print()
            print('===Results for your query:===')
            find_faq()
        elif choice == '4':
            print('===Delete FAQ===')
            delete_faq()
        elif choice == '5':
            print('Bye!')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == "__main__":
    faqs = load_faqs()
    main()
