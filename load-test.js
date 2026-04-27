import http from 'k6/http';
import { check } from 'k6';

export let options = {
  stages: [
    { duration: '10s', target: 20 },
    { duration: '20s', target: 50 },
    { duration: '20s', target: 100 },
  ],
};

const BASE_URL = 'http://localhost:8000';

export default function () {
  const payload = JSON.stringify({
    tradeId: Math.random().toString(),
    userId: "f412f236-4edc-47a2-8f54-8763a6ed2ce8",
    sessionId: "session-1",
    asset: "AAPL",
    assetClass: "equity",
    direction: "long",
    entryPrice: 100,
    exitPrice: 110,
    quantity: 1,
    entryAt: "2025-01-01T10:00:00Z",
    exitAt: "2025-01-01T10:05:00Z",
    status: "closed",
    outcome: "win",
    pnl: 10,
    planAdherence: 4,
    emotionalState: "calm"
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmNDEyZjIzNi00ZWRjLTQ3YTItOGY1NC04NzYzYTZlZDJjZTgiLCJpYXQiOjE3MTAwMDAwMDAsImV4cCI6MTk5OTk5OTk5OSwicm9sZSI6InRyYWRlciJ9.x5PYBb_YwoxFIa-lLXCcTGIsd1g1zqQlDihiUF_ebeA'
    },
  };

  let res = http.post(`${BASE_URL}/trades`, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}