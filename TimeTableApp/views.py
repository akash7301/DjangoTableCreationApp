from django.shortcuts import render,redirect,get_object_or_404
from TimeTableApp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Table
from .forms import TableForm
from django.contrib import messages
# Create your views here.

def sign_up_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('login')
    return render(request,'TimeTableApp/signup.html',locals())

@login_required
def home_view(request):
    tables = Table.objects.filter(user=request.user)

    if not tables:
        return render(request,'TimeTableApp/main_page.html')
    else:
        header_list = []
        table_list = []
        row_col = []
        for table in tables:
            row_col.append([table.rows,table.col])

        for table in tables:
            temp = []
            for i in range(int(table.col)):
                temp.append(table.table_data[i])
            header_list.append(temp)

        for table in tables:
            temp = []
            r = []
            k = 0
            for i in range(int(table.col),((int(table.rows)+1)*(int(table.col)))):
                temp.append(table.table_data[i])
                print(table.table_data[i])
                k += 1
                if k == int(table.col):
                    r.append(temp)
                    temp = []
                    k = 0
            table_list.append(r)

        all_table = []
        for h in header_list:
            temp = []
            temp.append(h)
            all_table.append(temp)
        for i,data in enumerate(table_list):
            all_table[i].append(data)
            all_table[i].append(tables[i].rows)
            all_table[i].append(tables[i].col)
            all_table[i].append(tables[i].id)
            all_table[i].append(tables[i].name)

        return render(request,'TimeTableApp/tablelist.html',locals())



@login_required
def createTableView(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    return render(request,'TimeTableApp/empty_table.html',locals())

@ login_required
def createDataTable(request):
    #if request.user.is_authenticated():
    current_user = request.user
    id = current_user.id
    data_list = []
    row=int(request.GET['a'])
    col=int(request.GET['b'])
    table_name = request.GET['table_name']
    for i in range(col):
        data_list.append(request.GET['h{}'.format(i)])
    for i in range(row):
        for j in range(col):
            data_list.append(request.GET['d{}{}'.format(i,j)])
    T = Table.objects.create(user=current_user,table_data=data_list,rows=row,col=col,name=table_name)
    T.save()
    one_list = T.table_data
    header = []
    r = []
    for i in range(col):
        header.append(one_list[i])
    k = 0
    temp = []
    for i in range(col,(row+1)*col):
        temp.append(one_list[i])
        k += 1
        if k==col:
            r.append(temp)
            temp = []
            k = 0
    return render(request,'TimeTableApp/data_table.html',locals())

@login_required
def editTableView(request,pk):
    current_user = request.user
    id = current_user.id
    data_list = []
    row=int(request.GET['a'])
    col=int(request.GET['b'])
    T = Table.objects.get(id=pk)
    one_list = T.table_data
    header = []
    r = []
    for i in range(col):
        header.append(one_list[i])
    k = 0
    temp = []
    for i in range(col,(row+1)*col):
        temp.append(one_list[i])
        k += 1
        if k==col:
            r.append(temp)
            temp = []
            k = 0
    return render(request,'TimeTableApp/edittable.html',locals())

@login_required
def updateTable(request,pk):
    current_user = request.user
    id = current_user.id
    data_list = []
    row=int(request.GET['a'])
    col=int(request.GET['b'])
    print('rowwwww : ',row)
    for i in range(col):
        data_list.append(request.GET['h{}'.format(i)])
    for i in range(row):
        for j in range(col):
            data_list.append(request.GET['d{}{}'.format(i,j)])
    #print(data_list)
    T = Table.objects.get(id=pk)
    T.rows = row
    T.col = col
    T.table_data=data_list
    T.save()
    one_list = T.table_data
    table_name = T.name
    header = []
    r = []
    for i in range(col):
        header.append(one_list[i])
    k = 0
    temp = []
    for i in range(col,(row+1)*col):
        temp.append(one_list[i])
        k += 1
        if k==col:
            r.append(temp)
            temp = []
            k = 0
    return render(request,'TimeTableApp/data_table.html',locals())

@login_required
def deleteTable(request,pk):
    table = Table.objects.get(id=pk)
    table.delete()
    messages.warning(request, 'You deleted one table!')
    return redirect('home')

def newTableView(request):
    return render(request,'TimeTableApp/main_page.html')
