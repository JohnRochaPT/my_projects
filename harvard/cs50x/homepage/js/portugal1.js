/// My own javascript file
function setMenu(home, lisbon, porto, algarve) {
    let name = document.title;
    console.log(name);

    /// Set navigation buttons
    if (name == "Portugal") {
        home.classList.add("active");
        document.querySelector("#subTitle1").innerHTML = "World class destination"
    } else if (name == "Lisbon") {
        lisbon.classList.add("active");
        document.querySelector("#subTitle1").innerHTML = "Lisbon - Lisboa"
    } else if (name == "Porto") {
        porto.classList.add("active");
        document.querySelector("#subTitle1").innerHTML = "Porto - O Porto"
    } else {
        algarve.classList.add("active");
        document.querySelector("#subTitle1").innerHTML = "Algarve - The Portuguese Riviera"
    }
}
