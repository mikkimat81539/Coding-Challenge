// Check to see if AM or PM is selected or stored in local storage or T/F -- DONE

// If am is selected hour should be (0 - 11) -- DONE
// if pm is selected hour should be (12 - 23) -- DONE

// EX: if 12:00 AM than 00:00 -- DONE
// EX: if 6:00 PM than 18:00 -- DONE

// grab the value of the hour and if True (PM) display (12 - 23) -- DONE

// Store hour and minutes in format ???
// if localTime == scheduled time

const am_pm = document.getElementById("sunrise"); 
const sendBtn = document.getElementById("send")
const userHour = document.getElementById("hour")

let timeBool = true // to see whether user selected AM or PM

sendBtn.addEventListener('click', sunTime)

function sunTime() {
	const sunValue = am_pm.value // grab the value of the selected AM/PM
	let int_hour = Number(userHour.value) // convert value into integers

	timeBool = (sunValue === "am") // if user selects AM than True

	// PM should be (12 - 23)
	if (!timeBool && int_hour !== 12) {
		int_hour += 12
		console.log(int_hour)	
	}

	// if 12 is selected and AM is selected than it should be 0
	else if (timeBool && int_hour === 12) {
		int_hour = 0
		console.log(int_hour)
	}

	// AM should be (1 - 11)
	else {
		console.log(int_hour)
	}
}

