from storage import save_faqs

def add_faq(faqs):
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

def show_faqs(faqs):
    if faqs:
        for i in range(len(faqs)):
            print(f'{i+1}. {faqs[i]["question"]}: \n {faqs[i]["answer"]}')
    else:
        print("No FAQs available")

def find_faq(faqs):
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

def delete_faq(faqs):
    if not faqs:
        print('No FAQ available')
    else:
        show_faqs(faqs)
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