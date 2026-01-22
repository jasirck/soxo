import { useEffect, useState } from "react";
import "./App.css";

const defaultColumns = [
  { id: 1, title: "To Do", tasks: [] },
  { id: 2, title: "In Progress", tasks: [] },
  { id: 3, title: "Done", tasks: [] },
];

export default function App() {
  const [columns, setColumns] = useState(
    JSON.parse(localStorage.getItem("kanban")) || defaultColumns
  );

  const [newColumn, setNewColumn] = useState("");
  const [taskInputs, setTaskInputs] = useState({});

  useEffect(() => {
    localStorage.setItem("kanban", JSON.stringify(columns));
  }, [columns]);

  const addColumn = () => {
    if (!newColumn) return;
    setColumns([...columns, { id: Date.now(), title: newColumn, tasks: [] }]);
    setNewColumn("");
  };

  const addTask = (colId) => {
    if (!taskInputs[colId]) return;

    setColumns(
      columns.map(col =>
        col.id === colId
          ? {
              ...col,
              tasks: [
                ...col.tasks,
                { id: Date.now(), text: taskInputs[colId] }
              ]
            }
          : col
      )
    );

    setTaskInputs({ ...taskInputs, [colId]: "" });
  };

  const deleteTask = (colId, taskId) => {
    setColumns(
      columns.map(col =>
        col.id === colId
          ? { ...col, tasks: col.tasks.filter(t => t.id !== taskId) }
          : col
      )
    );
  };

  const onDrop = (e, colId) => {
    const data = JSON.parse(e.dataTransfer.getData("task"));

    setColumns(
      columns.map(col => {
        if (col.id === data.from) {
          return {
            ...col,
            tasks: col.tasks.filter(t => t.id !== data.task.id)
          };
        }
        if (col.id === colId) {
          return { ...col, tasks: [...col.tasks, data.task] };
        }
        return col;
      })
    );
  };

  return (
    <div className="app-container">
      <div className="top-controls">
        <input
          placeholder="New column"
          value={newColumn}
          onChange={e => setNewColumn(e.target.value)}
        />
        <button onClick={addColumn}>Add Column</button>
      </div>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              {columns.map(col => (
                <th key={col.id}>{col.title}</th>
              ))}
            </tr>
          </thead>

          <tbody>
            <tr>
              {columns.map(col => (
                <td
                  key={col.id}
                  onDragOver={e => e.preventDefault()}
                  onDrop={e => onDrop(e, col.id)}
                >
                  {col.tasks.map(task => (
                    <div
                      key={task.id}
                      className="task"
                      draggable
                      onDragStart={e =>
                        e.dataTransfer.setData(
                          "task",
                          JSON.stringify({ task, from: col.id })
                        )
                      }
                    >
                      <span>{task.text}</span>
                      <button onClick={() => deleteTask(col.id, task.id)}>
                        x
                      </button>
                    </div>
                  ))}

                  <input
                    placeholder="New task"
                    value={taskInputs[col.id] || ""}
                    onChange={e =>
                      setTaskInputs({
                        ...taskInputs,
                        [col.id]: e.target.value
                      })
                    }
                  />
                  <button onClick={() => addTask(col.id)}>Add</button>
                </td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
