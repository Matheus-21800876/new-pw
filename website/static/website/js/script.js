let isDark = false;

function toggle() {
    if(!isDark) {
        document.documentElement.style.setProperty('--primary','black');
        document.documentElement.style.setProperty('--secondary','white');

        document.documentElement.style.setProperty('--terciary','#323232');
        document.documentElement.style.setProperty('--quartenary','#999');

    } else {
        document.documentElement.style.setProperty('--primary','white');
        document.documentElement.style.setProperty('--secondary','black');

        document.documentElement.style.setProperty('--terciary','#999');
        document.documentElement.style.setProperty('--quartenary','#323232');
    }
    isDark = !isDark;
}

function showSection(section) {

    fetch(`/sections/${section}`)
        .then(response => response.json())
        .then(text => {
            document.querySelector('#content').innerHTML = criaPaletas(text.paletas).join("");
        });
}

function criaPaletas(paletas) {
    paletasHTML = [];

    paletas.map((p) => { paletasHTML.push(templatePaleta(p)) });

    return paletasHTML;
}

function templatePaleta(paleta) {
    return template =
        `
            <section id="palette-section">
                <article class="small-palette-box">
                    <svg>
                        <rect class="color-line" fill="${paleta.color01}" x="0" y="0"></rect>
                        <g class="color-code">
                            <rect class="overlay" x="0" y="0"></rect>
                            <rect class="text-contrast" x="170" y="25"></rect>
                            <text x="180" y="45" fill="#fff">${paleta.color01}</text>
                        </g>
    
                        <rect class="color-line" fill="${paleta.color02}" x="0" y="50"></rect>
                        <g class="color-code">
                            <rect class="overlay" x="0" y="50"></rect>
                            <rect class="text-contrast" x="170" y="75"></rect>
                            <text x="180" y="95" fill="#fff">${paleta.color02}</text>
                        </g>
    
                        <rect class="color-line" fill="${paleta.color03}" x="0" y="100"></rect>
                        <g class="color-code">
                            <rect class="overlay" x="0" y="100"></rect>
                            <rect class="text-contrast" x="170" y="125"></rect>
                            <text x="180" y="145" fill="#fff">${paleta.color03}</text>
                        </g>
    
                        <rect class="color-line" fill="${paleta.color04}" x="0" y="150"></rect>
                        <g class="color-code">
                            <rect class="overlay" x="0" y="150"></rect>
                            <rect class="text-contrast" x="170" y="175"></rect>
                            <text x="180" y="195" fill="#fff">${paleta.color04}</text>
                        </g>
                    </svg>
                    <a href="#" onclick="paginaPaleta('${paleta.name}','${paleta.autor}','${paleta.color01}','${paleta.color02}','${paleta.color03}','${paleta.color04}')" class="palette-name">${paleta.name}</a>
                    <p class="palette-author">${paleta.autor}</p>
                </article>
            </section>         
                `;
}

function paginaPaleta(name, autor, color01, color02, color03, color04) {

    document.querySelector('#content').innerHTML =
        `
            <section id="palette-info">

                <h2>${name}</h2>
                <h3>Criada por ${autor}</h3>

                <section id="color-itens">
                    <article class="color-item">
                        <svg>
                            <rect fill="${color01}" width="200px" height="200px"></rect>
                        </svg>
                        <p>${color01}</p>
                    </article>

                    <article class="color-item">
                        <svg>
                            <rect fill="${color02}" width="200px" height="200px"></rect>
                        </svg>
                        <p>${color02}</p>
                    </article>

                    <article class="color-item">
                        <svg>
                            <rect fill="${color03}" width="200px" height="200px"></rect>
                        </svg>
                        <p>${color03}</p>
                    </article>

                    <article class="color-item">
                        <svg>
                            <rect fill="${color04}" width="200px" height="200px"></rect>
                        </svg>
                        <p>${color04}</p>
                    </article>
                </section>
            </section>
            `;
}

window.onload = function() {
    showSection(2);
}