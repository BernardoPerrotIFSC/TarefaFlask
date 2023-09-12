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