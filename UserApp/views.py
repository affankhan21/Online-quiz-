from django.shortcuts import render,redirect
from django.shortcuts import  get_object_or_404
from django.http import HttpResponse
from AdminApp.models import Subject,Question,Answer
from UserApp.models import UserInfo,Test
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def home(request):
    subject=Subject.objects.all()
    question=Question.objects.all()
    return render(request,"homepage.html",{'subject':subject,'question':question})

# def login(request):
#     if(request.method=="GET"):
#         return render(request,"login.html",{})
#     else:        
#         username = request.POST["uname"]
#         password = request.POST["pwd"]
#         try:
#             user = UserInfo.objects.get(username = username,password =password)            
#         except:
#             #Invalid credentials
#             return redirect(login)
#         else:
#             request.session["uname"]=username            
#             return redirect(homep)


# def register(request):
#     if(request.method=="GET"):
#         return render(request,"register.html",{})
#     else:        
#         username = request.POST["uname"]
#         password = request.POST["pwd"]
#         email = request.POST["email"]
#         try:            
#             user = UserInfo.objects.get(username = username)
#         except:
#             #If match not found, then this user is new user
#             #So we can create user account
#             user = UserInfo(username=username,password=password,email=email)
#             user.save()
#             return redirect(homep)

# def register(request):
#     if request.method == "GET":
#         return render(request, "register.html", {})
#     else:
#         username = request.POST["uname"]
#         password = request.POST["pwd"]
#         email = request.POST["email"]
#         hashed_password = make_password(password)  # Hash the password

#         try:
#             # Check if user already exists
#             user = UserInfo.objects.get(username=username)
#             # Handle case where user already exists
#             return render(request, "register.html", {"error_message": "Username already exists. Please choose a different one."})
#         except UserInfo.DoesNotExist:
#             # If match not found, then this user is a new user
#             # So we can create a user account with hashed password
#             user = UserInfo(username=username, password=hashed_password, email=email)
#             user.save()
#             return redirect(home)

def register(request):
    if request.method == "GET":
        return render(request, "register.html", {})
    else:
        username = request.POST["uname"]
        password = request.POST["pwd"]
        email = request.POST["email"]
        
        # Hash the password using a different algorithm, for example, MD5
        hashed_password = make_password(password, hasher='pbkdf2_sha256')
        
        try:
            # Check if user already exists
            user = UserInfo.objects.get(username=username)
            # Handle case where user already exists
            return render(request, "register.html", {"error_message": "Username already exists. Please choose a different one."})
        except UserInfo.DoesNotExist:
            # If match not found, then this user is a new user
            # So we can create a user account with hashed password
            user = UserInfo(username=username, password=hashed_password, email=email)
            user.save()
            return redirect(home)
# def login_vw(request):
#     if request.method == 'POST':
#         username = request.POST['uname']  # Updated key to 'uname'
#         password = request.POST['pwd'] 
#         print(username)
#         print(password)  
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             request.session["uname"]=username 
#             print(username)
#             return redirect(homep)
#         else:
#             # Return an 'invalid login' error message.
#             # return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
#             messages.error(request, 'Invalid username or password.')
#        # If request method is GET, render the login form.
#     return render(request, 'login.html', {})
# def login_vw(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         password = request.POST['pwd']
#         print(username)
#         print(password)
        
#         try:
#             # Get the user object from the database
#             user = UserInfo.objects.get(username=username)
#             print(user)
            
#             # Validate the password using the specified hashing algorithm
#             if check_password(password, user.password):
#                 # Password is correct, login the user
#                 login(request, user)
#                 # Redirect to a success page.
#                 request.session["uname"] = username 
#                 print(username)
#                 return redirect(homep)
#             else:
#                 # Password is incorrect
#                 messages.error(request, 'Invalid username or password.')
#         except UserInfo.DoesNotExist:
#             # User does not exist
#             messages.error(request, 'Invalid username or password.')
    
#     # If request method is GET or login fails, render the login form.
#     return render(request, 'login.html', {})

# def login_vw(request):
#     if request.method == 'POST':
#         username = request.POST['uname']
#         password = request.POST['pwd']
        
#         if not username or not password:
#             # Handle case where username or password is missing
#             messages.error(request, 'Please provide both username and password.')
#             return render(request, 'login.html', {})
        
#         try:
#             # Get the user object from the database
#             user = UserInfo.objects.get(username=username)
            
#             # Validate the password
#             if check_password(password, user.password):
#                 # Password is correct, login the user
#                 login(request, user)
#                 request.session["uname"] = username 
#                 return redirect(homep)
#             else:
#                 # Password is incorrect
#                 messages.error(request, 'Invalid username or password.')
#         except UserInfo.DoesNotExist:
#             # User does not exist
#             messages.error(request, 'Invalid username or password.')
#         except Exception as e:
#             # Handle any other exceptions
#             messages.error(request, f'An error occurred: {e}')
    
#     # If request method is GET or login fails, render the login form.
#     return render(request, 'login.html', {})
# from django.contrib import messages

# def login_vw(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')  # Using .get() to avoid KeyError
#         password = request.POST.get('pwd')
#         print("Username:", username)  # Print username for debugging
#         print("Password:", password)  # Print password for debugging
        
#         user = authenticate(request, username=username, password=password)
#         print("Authenticated User:", user)  # Print authenticated user for debugging

#         if user is not None:
#             login(request, user)
#             request.session["uname"] = username 
#             print("Logged in as:", username)  # Print logged-in username for debugging
#             return redirect(homep)
#         else:
#             messages.error(request, 'Invalid username or password.')
            
#     return render(request, 'login.html', {})
def login_vw(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(type(username))
        password = request.POST.get('pwd')
        print(type(password))

        # Retrieve user object from the database based on the username/email
        try:
            user = UserInfo.objects.get(username=username)
            print(type(user))
        except UserInfo.DoesNotExist:
            user = None

        if user is not None:
            # Retrieve the hashed password stored in the database
            hashed_password = user.password  # This is the hashed password

            # Check if the entered password matches the hashed password
            if check_password(password, hashed_password):
                # Passwords match, perform login
                login(request, user)
                request.session["uname"] = username 
                return redirect(homep)
            else:
                # Passwords don't match, display error message
                messages.error(request, 'Invalid username or password.')
        else:
            # User not found, display error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {})

def homep(request):
    if 'uname' not in request.session:
        # Redirect to login page if username is not in session
        return redirect('login')  # Assuming 'login' is the name of your login URL pattern
    
    username = request.session["uname"]
    subjects = Subject.objects.all()
    # subject = [Subject.objects.get(id=sid)] if Subject.objects.exists() else []
    sid_list = [subject.id for subject in subjects]

    question = Question.objects.all()
    answer=Answer.objects.all()
    return render(request, "homepage2.html", {'subjects': subjects,'subject': subjects,'sid_list': sid_list,  'question': question,'answer':answer, 'username': username})



# def viewSubjects(request, sid):
#         subject = Subject.objects.all()
#         subt = Subject.objects.get(id=sid)
#         question = Question.objects.filter(sname_id=sid)  # Corrected from sname_id to sid
#         answer = Answer.objects.filter(subt=subt)
#         return render(request, "homepage2.html", {"subject": subject, "subt": subt, 'question': question, 'answer': answer})


# def viewSubjects(request, sid):
#     subjects = Subject.objects.all()
#     subject = Subject.objects.get(id=sid)
#     questions = Question.objects.filter(sname=subject)
#     answers = Answer.objects.filter(question__in=questions)
#     return render(request, "homepage2.html", {"subjects": subjects, "subject": subject, "questions": questions, "answers": answers})
def viewSubjects(request,subject_id):
    subjects = Subject.objects.all()
    selected_subject_id = request.GET.get('subject_id')  # Get the selected subject ID from the query parameters
    if selected_subject_id:
        questions_with_answers = Question.objects.filter(subject_id=selected_subject_id).prefetch_related('answers')
    else:
        questions_with_answers = None
    return render(request, "homepage2.html", {"subjects": subjects, "questions_with_answers": questions_with_answers})

def select_subject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        # Redirect to another view along with the selected subject_id
        return redirect('another_view', subject_id=subject_id)
    else:
        return redirect('homep')  # Redirect back to the home page if the form is not submitted via POST

# def another_view(request, subject_id, question_number=1):
#     # Fetch the question based on the subject ID and question number
#     question = Question.objects.filter(sname_id=subject_id).order_by('id')[question_number - 1]
#     answers = Answer.objects.filter(question=question)

#     context = {
#         'question': question,
#         'answers': answers,
#          'question_number': question_number,
#     }
#     return render(request, 'an.html', context)

# def another_view(request, subject_id, question_number=1):
#     question = Question.objects.filter(sname_id=subject_id).order_by('id')[question_number - 1]
#     answers = Answer.objects.filter(question=question)

#     context = {
#         'question': question,
#         'answers': answers,
#         'question_number': question_number,
#     }
#     return render(request, 'an.html', context)
# def save_response(request):
#     if request.method == 'POST':
#         # Process and save user response
#         # Example code to handle user response
#         question_id = request.POST.get('question_id')
#         selected_answer_id = request.POST.get('selected_answer_id')
#         # Save user response logic here

#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False})

# def another_view(request, subject_id, question_number):
#     # Get the subject
#     subject = get_object_or_404(Subject, pk=subject_id)

#     # Get all questions for the subject
#     questions = Question.objects.filter(sname=subject)

#     # Get answer marks for each question
#     question_marks = {}
#     for question in questions:
#         # Get correct answer for the question
#         correct_answer = Answer.objects.filter(question=question, is_correct=True).first()
#         if correct_answer:
#             # Calculate marks for the question
#             question_marks[question] = correct_answer.question.marks if correct_answer else 0
#         else:
#             question_marks[question] = 0

#     context = {
#         'subject': subject,
#         'questions': questions,
#         'question_marks': question_marks,
#         'question_number': question_number,
#     }
#     return render(request, 'an.html', context)
# 
# def another_view(request, subject_id):
#     # Get the subject
#     subject = get_object_or_404(Subject, pk=subject_id)

#     # Get all questions for the subject
#     questions = Question.objects.filter(sname=subject)

#     # Get answers for each question
#     answers = {}
#     for question in questions:
#         answers[question.id] = Answer.objects.filter(question=question)

#     context = {
#         'subject': subject,
#         'questions': questions,
#         'answers': answers
#     }
#     return render(request, 'an.html', context)
def another_view(request, subject_id):
    # Get the subject
    subject = get_object_or_404(Subject, pk=subject_id)

    # Get all questions for the subject
    questions = Question.objects.filter(sname=subject)

    # Get answers for each question
    answers = {}
    for question in questions:
        answers[question.id] = Answer.objects.filter(question=question)

    context = {
        'subject': subject,
        'questions': questions,
        'answers': {question.id: Answer.objects.filter(question=question) for question in questions}
    }
    # print(answers)
    # return render(request, 'an.html', context)
    return render(request, 'an2.html', context)



# def final(request):
#     if request.method == 'POST':
#         username = request.session.get("uname")
#         if not username:
#             return HttpResponse("Username not found in request")

#         questions_with_answers = []

#         for question in Question.objects.all():
#             selected_answer_id = request.POST.get(f"question_{question.id}")
#             selected_answer = None
#             is_correct = False
            
#             if selected_answer_id:
#                 selected_answer = get_object_or_404(Answer, pk=int(selected_answer_id))
#                 is_correct = selected_answer.is_correct
            
#             # Fetch the correct answer for the question
#             correct_answer = Answer.objects.filter(question=question, is_correct=True).first()

#             questions_with_answers.append({
#                 'question': question, 
#                 'selected_answer': selected_answer, 
#                 'correct_answer': correct_answer,
#                 'is_correct': is_correct
#             })
#             print(username)
#             print(questions_with_answers)
#             print(selected_answer_id)
          
#         total_marks = sum(item['question'].marks if item['is_correct'] else 0 for item in questions_with_answers)
#         print(total_marks)
#         return render(request, 'final.html', {'username': username, 'questions_with_answers': questions_with_answers, 'total_marks': total_marks})
#     else:
#         return HttpResponse("Method not allowed", status=405)

# def final(request):
#     if request.method == 'POST':
#         username = request.session.get("uname")
#         subject_id = request.POST.get('subject_id')  # Assuming you're getting subject_id from the form
#         if not username:
#             return HttpResponse("Username not found in request")
#         if not subject_id:
#             return HttpResponse("Subject ID not found in request")
        
#         questions_with_answers = []

#         for question in Question.objects.filter(sname_id=subject_id):  # Filter questions based on subject ID
#             selected_answer_id = request.POST.get(f"question_{question.id}")
#             selected_answer = None
#             is_correct = False
            
#             if selected_answer_id:
#                 selected_answer = get_object_or_404(Answer, pk=int(selected_answer_id))
#                 is_correct = selected_answer.is_correct
            
#             # Fetch the correct answer for the question
#             correct_answer = Answer.objects.filter(question=question, is_correct=True).first()

#             questions_with_answers.append({
#                 'question': question, 
#                 'selected_answer': selected_answer, 
#                 'correct_answer': correct_answer,
#                 'is_correct': is_correct
#             })
#             print(username)
#             print(questions_with_answers)
#             print(selected_answer_id)
          
#         total_marks = sum(item['question'].marks if item['is_correct'] else 0 for item in questions_with_answers)
#         print(total_marks)
#         return render(request, 'final.html', {'username': username, 'questions_with_answers': questions_with_answers, 'total_marks': total_marks})
#     else:
#         return HttpResponse("Method not allowed", status=405)



def final(request):
    if request.method == 'POST':
        # Retrieve subject information from POST data
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')

        # Retrieve username from session
        username = request.session.get("uname")
        if not username:
            return HttpResponse("Username not found in request")

        # Fetch questions related to the subject
        questions = Question.objects.filter(sname_id=subject_id)
        if not questions.exists():
            return HttpResponse("Questions not found for the subject")

        # Initialize list to store questions with answers
        questions_with_answers = []

        # Iterate through questions and process answers
        for question in questions:
            selected_answer_id = request.POST.get(f"question_{question.id}")
            selected_answer = None
            is_correct = False
            
            if selected_answer_id:
                selected_answer = get_object_or_404(Answer, pk=int(selected_answer_id))
                is_correct = selected_answer.is_correct
            
            # Fetch the correct answer for the question
            correct_answer = Answer.objects.filter(question=question, is_correct=True).first()

            questions_with_answers.append({
                'question': question, 
                'selected_answer': selected_answer, 
                'correct_answer': correct_answer,
                'is_correct': is_correct
            })

        # Calculate total marks
        total_marks = sum(item['question'].marks if item['is_correct'] else 0 for item in questions_with_answers)

        # Pass subject information and other data to final.html
        return render(request, 'final.html', {
            'username': username,
            'subject_id': subject_id,
            'subject_name': subject_name,
            'questions_with_answers': questions_with_answers,
            'total_marks': total_marks
        })
    else:
        return HttpResponse("Method not allowed", status=405)
def logout(request):
    request.session.clear()
    return redirect(login_vw)
