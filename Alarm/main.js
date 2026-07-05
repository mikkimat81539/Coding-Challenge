const am_pm = document.getElementById("sunrise"); 
const sendBtn = document.getElementById("send")

// if AM is selected display sunrise in the console
// if PM is selected display sunset in the console

sendBtn.addEventListener('click', sunTime)

function sunTime() {
	const sunValue = am_pm.value

	console.log(sunValue)

}

