import { useState } from "react";
import ReactMarkdown from "react-markdown";

function App() {
  const [jobDesc, setJobDesc] = useState("");
  const [resume, setResume] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const analyze = async () => {
    if (!jobDesc || !resume) {
      alert("请填写职位描述和简历内容");
      return;
    }
    setLoading(true);
    setResult("");

    const response = await fetch("https://resume-analyzer-production-9386.up.railway.app/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        job_description: jobDesc,
        resume: resume,
      }),
    });

    const data = await response.json();
    setResult(data.result);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", padding: "0 20px", fontFamily: "sans-serif" }}>
      <h1>🤖 AI简历分析器</h1>

      <h3>职位描述</h3>
      <textarea
        rows={6}
        style={{ width: "100%", padding: 10, fontSize: 14 }}
        placeholder="粘贴职位描述..."
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
      />

      <h3>简历内容</h3>
      <textarea
        rows={10}
        style={{ width: "100%", padding: 10, fontSize: 14 }}
        placeholder="粘贴简历内容..."
        value={resume}
        onChange={(e) => setResume(e.target.value)}
      />

      <button
        onClick={analyze}
        style={{
          marginTop: 16,
          padding: "12px 32px",
          fontSize: 16,
          background: "#4F46E5",
          color: "white",
          border: "none",
          borderRadius: 8,
          cursor: "pointer",
        }}
      >
        {loading ? "分析中..." : "开始分析"}
      </button>

      {result && (
        <div style={{ marginTop: 32, padding: 20, background: "#f9f9f9", borderRadius: 8, whiteSpace: "pre-wrap" }}>
          <h3>分析结果</h3>
          <ReactMarkdown>{result}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;