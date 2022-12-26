/*




let staffList = [
    {
        id: 1,
        name: "Abbos",
        description: 'Task name',
        startDate: 'date',
        endDate: 'date',
        status: 'Pending'
    },
    {
        id: 2,
        name: "Doston",
        description: 'Task name 2',
        startDate: 'date 2',
        endDate: 'date 2',
        status: 'Doing'
    },
    {
        id: 4,
        name: "Vali",
        description: "Task name 3",
        startDate: 'date 3',
        endDate: 'date 3',
        status: 'Done'
    },
    {
        id: 4,
        name: "Ozodbek",
        description: 'Task name 4',
        startDate: 'date 4',
        endDate: 'date 4',
        status: 'Rejected'
    }
];

function getStaffList() {
    document.getElementById('pendingList').innerHTML = '';
    document.getElementById('doingList').innerHTML = '';
    document.getElementById('doneList').innerHTML = '';
    document.getElementById('rejectedList').innerHTML = '';

    for (let i=0; i<staffList.length; i++){
        if (staffList[i].status ==='Pending'){
            document.getElementById('pendingList').innerHTML += '' +
                '<div class="name">' + staffList[i].name + '</div>'+

                '<div class="task-name">' + staffList[i].description + '</div>'+

                '<div class="start-date">' +
                '      <div class="text">start date:</div>' +
                '      <div class="date text-success">'+ staffList[i].startDate +'</div>' +
                '</div>'+

                '<div class="end-date">' +
                '      <div class="text">end date:</div>' +
                '      <div class="date text-danger">'+ staffList[i].endDate +'</div>' +
                '</div>'+

                '<select onchange="selectStatus('+1+', '+i+')" id="pendingSelect" class="form-control my-3">'+
                '<option selected disabled >Select status</option>'+
                '<option value="Doing">Doing</option>'+
                '<option value="Done">Done</option>'+
                '</select>'+

                '<div class="button-box">'+
                '<button onclick="editStaff()" class="btn btn-warning" type="button">Edit</button>'+
                '<button onclick="deleteTaskList('+i+')" class="btn btn-danger" type="button">Delete</button>'+
                '</div>'+
                '<hr>'
        }
        else if(staffList[i].status ==='Doing'){
            document.getElementById('doingList').innerHTML += '' +
                '<div class="name">' + staffList[i].name +'</div>'+
                '<div class="task-name">'+ staffList[i].description +'</div>'+

                '<div class="start-date">' +
                '      <div class="text">start date:</div>' +
                '      <div class="date text-success">'+ staffList[i].startDate +'</div>' +
                '</div>'+

                '<div class="end-date">' +
                '      <div class="text">end date:</div>' +
                '      <div class="date text-danger">'+ staffList[i].endDate +'</div>' +
                '</div>'+

                '<select onchange="selectStatus('+2+', '+i+')" id="doingSelect" class="form-control my-3">'+
                '<option selected disabled>Select status</option>'+
                '<option value="Pending">Pending</option>'+
                '<option value="Done">Done</option>'+
                '</select>'+

                '<div class="button-box">'+
                '<button onclick="editStaff()" class="btn btn-warning" type="button">Edit</button>'+
                '<button onclick="deleteTaskList('+i+')" class="btn btn-danger" type="button">Delete</button>'+
                '</div>'+
                '<hr>'
        }
        else if(staffList[i].status ==='Done'){
            document.getElementById('doneList').innerHTML += '' +
                '<div class="name">' + staffList[i].name +'</div>'+
                '<div class="task-name">'+ staffList[i].description +'</div>'+

                '<div class="start-date">' +
                '      <div class="text">start date:</div>' +
                '      <div class="date text-success">'+ staffList[i].startDate +'</div>' +
                '</div>'+

                '<div class="end-date">' +
                '      <div class="text">end date:</div>' +
                '      <div class="date text-danger">'+ staffList[i].endDate +'</div>' +
                '</div>'+


                '<div class="button-box">'+
                '<button class="btn btn-secondary mt-2" type="button">Rejected</button>'+
                '</div>'+
                '<hr>'
        }
        else if(staffList[i].status ==='Rejected'){
            document.getElementById('rejectedList').innerHTML += '' +
                '<div class="name">' + staffList[i].name +'</div>'+
                '<div class="task-name">'+ staffList[i].description +'</div>'+

                '<div class="start-date">' +
                '      <div class="text">start date:</div>' +
                '      <div class="date text-success">'+ staffList[i].startDate +'</div>' +
                '</div>'+

                '<div class="end-date">' +
                '      <div class="text">end date:</div>' +
                '      <div class="date text-danger">'+ staffList[i].endDate +'</div>' +
                '</div>'+

                '<select onchange="selectStatus('+3+', '+i+')" id="rejectedSelect" class="form-control my-3">'+
                '<option selected disabled>Select status</option>'+
                '<option value="Pending">Pending</option>'+
                '<option value="Doing">Doing</option>'+
                '<option value="Done">Done</option>'+
                '</select>'+

                '<div class="button-box">'+
                '<button onclick="editStaff()" class="btn btn-warning" type="button">Edit</button>'+
                '</div>'+
                '<hr>'
        }
        else{
            console.log("xato status");
        }
    }
}

getStaffList();


function deleteTaskList(index) {
    staffList.splice(index, 1);
    getStaffList();
}


function addStaffList() {
    let ism = document.getElementById('selectname').value;
    let task = document.getElementById('description').value;
    let start_Date = document.getElementById('startDate').value;
    let end_Date = document.getElementById('endDate').value;
    let statusTask = document.getElementById('selectStatus').value;


    if (ism !=='' && task !=='' && start_Date !=='' && end_Date !=='' && statusTask !==''){
        let newStaff = {
            id: staffList.length+1,
            name: ism,
            description: task,
            startDate: start_Date,
            endDate: end_Date,
            status: statusTask
        };

        staffList.push(newStaff);
        getStaffList();
        document.forms['myForm'].reset();
    }
    else{
        alert("Formani to'liq to'ldiring");
    }

}



let select = '';
let editedIndex = -1;
function selectStatus(name, index) {
    editedIndex = index;
    console.log(staffList[editedIndex].status);
    if (name === 1){
        select = document.getElementById('pendingSelect').value;
        staffList[editedIndex].status = select;
        console.log(select);
    }
    else if (name === 2){
        select = document.getElementById('doingSelect').value;
        staffList[editedIndex].status = select;
        console.log(select);
    }
    else{
        select = document.getElementById('rejectedSelect').value;
        staffList[editedIndex].status = select;
        console.log(select);
    }
}

function editStaff() {
    if(select !==''){
        getStaffList();
    }
    else{
        alert("Statusni tanlang !!!");
    }
}
*/

let count = 0;

document.getElementById('count').innerHTML = count;
document.getElementById('range').value = 0;

function addCount() {
    if (count !==100){
        count= parseInt(count)+1;
        document.getElementById('count').innerHTML = count;
        document.getElementById('range').value = count;
    }
    else{
        alert("Max = 100");
    }
}

function removeCount() {
    if (count !==0){
        count = count -1;
        document.getElementById('count').innerHTML = count;
        document.getElementById('range').value = count;
    }
    else{
        alert("Min = 0")
    }
}


function Counter() {
    count = document.getElementById('range').value;
    document.getElementById('count').innerHTML = count;
}

let width1 = 0;
let width2 = 0;
let width3 = 0;
let width4 = 0;

document.getElementById('progBar').style.width = '0%';
function myFunction(index) {
    if (index == 1) {
        if (width1 === 25) {
            width1 = 0;
        } else {
            width1 = 25;
        }
    }
    else if (index == 2) {
        if (width2 === 25) {
            width2 = 0;
        } else {
            width2 = 25;
        }
    }
    else if (index == 3) {
        if (width3 === 25) {
            width3 = 0;
        } else {
            width3 = 25;
        }
    }
    else {
        if (width4 === 25) {
            width4 = 0;
        } else {
            width4 = 25;
        }
    }

    document.getElementById('progBar').style.width= width1+width2+width3+width4+"%";
};



