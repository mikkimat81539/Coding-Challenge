/* Check to see if AM or PM is selected or stored in local storage or T/F -- DONE

If am is selected hour should be (0 - 11) -- DONE
if pm is selected hour should be (12 - 23) -- DONE

EX: if 12:00 AM than 00:00 -- DONE
EX: if 6:00 PM than 18:00 -- DONE

grab the value of the hour and if True (PM) display (12 - 23) -- DONE

Store hour and minutes in format -- DONE
if localTime == scheduled time -- DONE 

Add sound
store times in sorted list -- DONE

use Local storage for timer

Extra (create another fieldset):
- Add lists of sound to select from
- set date and time

*/

// Define Variables
const am_pm = document.getElementById("sunrise"); 
const sendBtn = document.getElementById("send")
const userHour = document.getElementById("hour")
const userMin = document.getElementById("minutes")

let timeBool = true // to see whether user selected AM or PM

const timeList = [] // Store multiple times in a list

sendBtn.addEventListener('click', sunTime)

function sunTime() {
	const sunValue = am_pm.value // grab the value of the selected AM/PM
	let int_hour = Number(userHour.value) // convert value into integers
	let int_min = Number(userMin.value)

	timeBool = (sunValue === "am") // if user selects AM than True

	const localHour = new Date().getHours()
	const localMin = new Date().getMinutes()

	const localTime = `${String(localHour).padStart(2, "0")}:${String(localMin)}`

	// PM should be (13 - 23)
	if (!timeBool && int_hour !== 12) {
		int_hour += 12
		let schedule_time = `${String(int_hour).padStart(2, "0")}:${String(int_min).padStart(2, '0')}`
	
		timeList.push(schedule_time)
		// console.log(timeList)

		/*if (localTime === schedule_time){

			console.log(true)}*/

	}

	// if 12 is selected and AM is selected than it should be 0
	else if (timeBool && int_hour === 12) {
		int_hour = 0
		let schedule_time = `${String(int_hour).padStart(2, "0")}:${String(int_min).padStart(2, '0')}`

		timeList.push(schedule_time)
		// console.log(timeList)

		/*if (localTime === schedule_time){

			console.log(true)}*/

	}

	// if 12 is selected and PM is selected than it should be 12
	else if (!timeBool && int_hour === 12) {
		int_hour = 12
		let schedule_time = `${String(int_hour).padStart(2, "0")}:${String(int_min).padStart(2, '0')}`

		timeList.push(schedule_time)
		// console.log(timeList)

		/*if (localTime === schedule_time){

			console.log(true)}*/

	}

	// AM should be (1 - 11)
	else {
		let schedule_time = `${String(int_hour).padStart(2, "0")}:${String(int_min).padStart(2, '0')}`

		timeList.push(schedule_time)
		// console.log(timeList)

		/*if (localTime === schedule_time){

			console.log(true)}*/

	}

	timeList.sort()

	let counter = 1

	for (let i = 0; i < timeList.length; i++){
			localStorage.setItem(`Time ${counter}`, timeList[i])

			counter += 1			

			if (i == localTime) {
				console.log(true)
			}
	}
	console.log(timeList)
}

