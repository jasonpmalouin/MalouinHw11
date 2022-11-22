window.addEventListener("load", onLoad);
var header = document.getElementsByClassName("header");
var container = document.getElementsByClassName("container");

function onLoad()
{
	document.body.classList.add("fade");
	header[0].addEventListener("mouseover", onHeaderHover);
	container[0].addEventListener("mouseover", onContainerHover);
	header[0].addEventListener("mouseout", onHeaderHover);
	container[0].addEventListener("mouseout", onContainerHover);
}

function onHeaderHover()
{
	header[0].classList.toggle("headerHover");
}

function onContainerHover()
{
	container[0].classList.toggle("containerHover");
}

