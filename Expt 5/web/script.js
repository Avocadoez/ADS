eel.expose(updatePlot);

let container = document.querySelector('.container')
let gallery = document.querySelector('.gallery')
let plotImageNumber = undefined

function updatePlot(graphNumber) {
    eel.generate_plot(graphNumber)(({name, url}) => {
        let plot = document.createElement('div')
        plot.classList.add('plot')
        plot.name = name
        plot.url = url
        plot.number = graphNumber
        plot.style.backgroundImage = `url("${url}")`;
        container.appendChild(plot)

        plot.onclick = (e) => {
            display_gallery(plot)
        }
    });
}

function display_gallery(plot) {
    console.log(plot.number);
    plotImageNumber = plot.number
    gallery.querySelector('.name').innerText = (plot.number + 1) + ". " + plot.name
    gallery.querySelector('.image').style.backgroundImage = `url("${plot.url}")`;
    gallery.style.display = 'flex'

}

// Call the function when the page loads
window.onload = () => {
    for (let i = 0; i < 11; i++) {
        updatePlot(i);
    }
};

document.addEventListener('keypress', (e) => {
    console.log(e.key);
    if (e.keyCode == 13) gallery.style.display = 'none'
    else if (e.keyCode == 37) moveSlider('left')
    else if (e.keyCode == 39) moveSlider('right')
})

gallery.querySelector('.right').onclick = () => moveSlider('right')
gallery.querySelector('.left').onclick = () => moveSlider('left')

function moveSlider(dir) {
    let plots = document.querySelectorAll('.plot')
    for (let i = 0; i < plots.length; i++) {
        let index = dir == 'left'? 
            plotImageNumber == 0? plots.length - 1 : plotImageNumber - 1 :
            dir == 'right'? (plotImageNumber + 1) % plots.length : 0
        if (plots[i].number == index) return display_gallery(plots[index])
    }
}