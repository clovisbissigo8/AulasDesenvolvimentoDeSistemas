from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Dict

app = FastAPI()

# modelo
class Tarefa(BaseModel):
    titulo: str = Field(..., min_length=3)
    descricao: Optional[str] = None
    concluida: bool = False
    id: Optional[int] = None

# banco na memoria
db_tarefas: Dict[int, Tarefa] = {}
_next_id = 1

def gerar_id():
    global _next_id
    task_id = _next_id
    _next_id += 1
    return task_id

# endpoint

# Criar tarefa
@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    if not tarefa.titulo or tarefa.titulo.strip() == "":
        raise HTTPException(status_code=400, detail="Título inválido")

    task_id = gerar_id()
    tarefa.id = task_id
    db_tarefas[task_id] = tarefa
    return tarefa

# Listar tarefas
@app.get("/tarefas")
def listar_tarefas():
    return list(db_tarefas.values())

# Buscar tarefa por id
@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    if id not in db_tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_tarefas[id]

# Atualizar tarefa
@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa: Tarefa):
    if id not in db_tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa.id = id
    db_tarefas[id] = tarefa
    return tarefa

# Deletar tarefa
@app.delete("/tarefas/{id}", status_code=204)
def deletar_tarefa(id: int):
    if id not in db_tarefas:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    del db_tarefas[id]
    return


