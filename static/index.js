function hypotenuse() {
    var number1 = document.getElementById("number1").value;
    var number2 = document.getElementById("number2").value;

    axios({
        method: "POST",
        url: "/hypotenuse",
        data: {
            number1: number1,
            number2: number2,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    )
}

function gpaConverter() {
    var number = document.getElementById("number").value;

    axios({
        method: "POST",
        url: "/gpaconverter",
        data: {
            number: number,
        },
        headers: {
            "Content-Type": "application/json",
        },
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    )
}

function squareRoot() {
    var number = document.getElementById("number").value;

    axios({
        method: "POST",
        url: "/squareroot",
        data: {
            number: number,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            document.getElementById("result").innerHTML = result["result"];
        },
        (error) => {
            console.log(error);
        }
    )
}

