# 🔢 INTERACTIVE SORTING ALGORITHM VISUALIZER

A clean, interactive web app to **visualize popular sorting and graph traversal algorithms** in real time — watch how each algorithm works step by step with smooth animations.

---

## ✨ Features

- 🎞️ Real-time animated visualization of sorting and graph algorithms
- 📊 10 sorting algorithms + 3 graph traversal algorithms
- ⚙️ Adjustable array size and animation speed
- 🎨 Color-coded bars for comparisons, swaps, and sorted elements
- 🔀 Randomize array with a single click
- 🗺️ Interactive graph visualizer with node traversal highlighting
- 📱 Responsive design — works on desktop and mobile

---

## 🧮 Sorting Algorithms

| Algorithm       | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity |
|----------------|------------------------|--------------------------|------------------|
| Bubble Sort     | O(n)                   | O(n²)                    | O(1)             |
| Selection Sort  | O(n²)                  | O(n²)                    | O(1)             |
| Insertion Sort  | O(n)                   | O(n²)                    | O(1)             |
| Merge Sort      | O(n log n)             | O(n log n)               | O(n)             |
| Quick Sort      | O(n log n)             | O(n²)                    | O(log n)         |
| Heap Sort       | O(n log n)             | O(n log n)               | O(1)             |
| Shell Sort      | O(n log n)             | O(n²)                    | O(1)             |
| Counting Sort   | O(n + k)               | O(n + k)                 | O(k)             |
| Radix Sort      | O(nk)                  | O(nk)                    | O(n + k)         |
| Tim Sort        | O(n)                   | O(n log n)               | O(n)             |

## 🗺️ Graph Algorithms

| Algorithm              | Description                                      | Time Complexity |
|-----------------------|--------------------------------------------------|-----------------|
| BFS (Breadth-First)   | Explores neighbors level by level                | O(V + E)        |
| DFS (Depth-First)     | Explores as deep as possible before backtracking | O(V + E)        |
| Dijkstra's            | Finds shortest path between nodes                | O(V² / E log V) |

---

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- [Node.js](https://nodejs.org/) *(if running a dev server)*

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sorting-visualizer.git

# Navigate into the project
cd sorting-visualizer

# Install dependencies (if applicable)
npm install

# Start the development server
npm start
```

Or simply open `index.html` directly in your browser — no server required.

---

## 🎮 How to Use

1. **Select an algorithm** from the dropdown menu
2. **Adjust the array size** using the size slider
3. **Set the speed** using the speed slider
4. Click **Generate New Array** to randomize the bars
5. Click **Sort** to start the visualization
6. Watch the algorithm work its magic! 🎉


---

## 🗂️ Project Structure

```
sorting-visualizer/
├── index.html              # Main HTML file
├── style.css               # Styling
├── main.js                 # Core logic & UI controls
├── sorting/
│   ├── bubbleSort.js
│   ├── selectionSort.js
│   ├── insertionSort.js
│   ├── mergeSort.js
│   ├── quickSort.js
│   ├── heapSort.js
│   ├── shellSort.js
│   ├── countingSort.js
│   ├── radixSort.js
│   └── timSort.js
├── graph/
│   ├── bfs.js
│   ├── dfs.js
│   └── dijkstra.js
└── README.md
```

---

## 🛠️ Built With

- **HTML5** — Structure
- **CSS3** — Styling & animations
- **Vanilla JavaScript** — Logic & DOM manipulation

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repo, then create a feature branch
git checkout -b feature/add-new-algorithm

# Commit your changes
git commit -m "Add: Shell Sort algorithm"

# Push to your fork
git push origin feature/add-new-algorithm

# Open a Pull Request 🚀
```

Please make sure your code is clean, commented, and consistent with the existing style.

---

## 📋 Roadmap

-  Sorting algorithms (Bubble, Selection, Insertion, Merge, Quick, Heap, Shell, Counting, Radix, Tim)
-  Graph algorithms (BFS, DFS, Dijkstra's)
-  Show step counter and swap count



---

## 👤 Author

INDIRAJITH.R
JAYANTH.E
NAVNEETH MOHAN
HARISH KARTHIK


---


