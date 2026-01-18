// Função para carregar os dados da ficha na lateral
function atualizarFichaLateral() {
    const atributos = ['agi', 'eng', 'fur', 'lut', 'esq'];
    atributos.forEach(attr => {
        const val = localStorage.getItem(`finnley_${attr}`) || 0;
        const elem = document.getElementById(`stat-${attr}`);
        if (elem) elem.innerText = val;
    });
}

// Função de Teste de Atributo Universal
function realizarTeste(atributo, dificuldade) {
    const bonus = parseInt(localStorage.getItem(`finnley_${atributo}`)) || 0;
    const dado = Math.floor(Math.random() * 20) + 1;
    const total = dado + bonus;
    
    const resultadoDiv = document.getElementById('resultado-rolagem') || document.getElementById('resultado-teste');
    
    let mensagem = "";
    let passou = total >= dificuldade;

    if (dado === 20) {
        mensagem = `✨ CRÍTICO! (20) + ${bonus} = ${total}! Sucesso Absoluto.`;
        passou = true;
    } else if (dado === 1) {
        mensagem = `💀 FALHA CRÍTICA! (1) + ${bonus} = ${total}...`;
        passou = false;
    } else {
        mensagem = `Rolagem: ${dado} + Bônus: ${bonus} = Total: ${total} (Dif: ${dificuldade})`;
    }

    if (resultadoDiv) {
        resultadoDiv.innerHTML = `<p style="color: ${passou ? '#4CAF50' : '#ff4500'}; font-weight: bold;">${mensagem}</p>`;
    }
    
    return passou;
}

document.addEventListener('DOMContentLoaded', atualizarFichaLateral);