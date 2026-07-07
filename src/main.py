faqs = []

def add_faq():
    question = input('Enter question: ')
    answer = input('Enter answer: ')

    faq = {'question': question, 'answer': answer}
    faqs.append(faq)
    print('FAQ added!')

def show_faqs():
    if len(faqs) > 0:
        for i in range(len(faqs)):
            print(f'{i+1}. {faqs[i]["question"]}: \n {faqs[i]["answer"]}')
    elif len(faqs) == 0:
        print("No FAQs available")

def find_faq():
    request = input("Enter search request: ").lower()
    coincidence = []

    for faq in faqs:
        if request in faq["question"].lower():
            coincidence.append(faq)

    if len(coincidence) > 0:
        for i in range(len(coincidence)):
            print(f"{i + 1}. {coincidence[i]['question']}:")
            print(f"   {coincidence[i]['answer']}\n")
    else:
        print("No matching FAQs found.")

def delete_faq():
    if not faqs:
        print('No FAQ available')
    else:
        show_faqs()
        print('Enter FAQ number to delete:')
        number = int(input())
        del faqs[number-1]
        print('FAQ deleted!')



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
    main()
