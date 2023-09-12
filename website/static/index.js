function deleteTarefa(tarefaId) {
    fetch("/delete-Tarefa", {
        method: "POST",
        body: JSON.stringify({tarefaId: tarefaId}),
    }).then(() => {
        window.location.href = "/"
    });
}
function alteraConcluido(tarefaId) {
    fetch("/altera-concluido", {
        method:"POST",
        body: JSON.stringify({tarefaId: tarefaId}),
    }).then(()=> {
        window.location.href ="/"
    })
}
function alteraAfazer(tarefaId) {
    fetch("/altera-afazer", {
        method:"POST",
        body: JSON.stringify({tarefaId: tarefaId}),
    }).then(()=> {
        window.location.href ="/"
    })
}
function alteraNenhum(tarefaId) {
    fetch("/altera-nenhum", {
        method:"POST",
        body: JSON.stringify({tarefaId: tarefaId}),
    }).then(()=> {
        window.location.href ="/"
    })
}

const filterForm = document.getElementById('filter-form');

filterForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(filterForm);
    const response = await fetch('/filtrar', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const data = await response.text();
        document.body.innerHTML = data;
    }
});
