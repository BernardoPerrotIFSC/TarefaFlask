function deleteTarefa(tarefaId) {
    fetch("/delete-Tarefa", {
        method: "POST",
        body: JSON.stringify({tarefaId: tarefaId}),
    }).then(() => {
        window.location.href = "/"
    });
}