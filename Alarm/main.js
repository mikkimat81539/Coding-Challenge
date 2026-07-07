// Check to see if AM or PM is selected or stored in local storage or T/F

// If am is selected hour should be (0 - 11)
// if pm is selected hour should be (12 - 23)

// EX: if 12:00 AM than 00:00
// EX: if 6:00 PM than 18:00

// grab the value of the hour and if True (PM) display (12 - 23)

const am_pm = document.getElementById("sunrise"); 
const sendBtn = document.getElementById("send")
const userHour = document.getElementById("hour")

let timeBool = true

sendBtn.addEventListener('click', sunTime)

function sunTime() {
	const sunValue = am_pm.value
	let int_hour = Number(userHour.value);

	timeBool = (sunValue === "am")

	if (!timeBool && int_hour !== 12) {
		int_hour += 12;
		console.log(int_hour)	
	}

	else {
		console.log(int_hour)
	}
}

