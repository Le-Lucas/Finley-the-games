function mostrarLore() {
  document.getElementById("intro").classList.add("oculto");
  document.getElementById("lore").classList.remove("oculto");
}

function mostrarRegras() {
  document.getElementById("lore").classList.add("oculto");
  document.getElementById("regras").classList.remove("oculto");
}
let pontos = 10;
const atributos = { agi:0, fur:0, eng:0, lut:0, esq:0 };

function toggleFicha() {
  document.getElementById("ficha").classList.toggle("oculto");
}

function mais(attr) {
  if (pontos > 0) {
    atributos[attr]++;
    pontos--;
    atualizarFicha();
  }
}

function menos(attr) {
  if (atributos[attr] > 0) {
    atributos[attr]--;
    pontos++;
    atualizarFicha();
  }
}

function atualizarFicha() {
  for (let a in atributos) {
    document.getElementById(a).textContent = atributos[a];
  }

  document.getElementById("pontos").textContent =
    "Pontos disponíveis: " + pontos;

  const btn = document.getElementById("btnDesafio");

  if (pontos === 0) {
    btn.disabled = false;
    btn.classList.remove("bloqueado");
  } else {
    btn.disabled = true;
    btn.classList.add("bloqueado");
  }
}
