# Real-Time API Monitoring and Latency Analytics Dashboard

A cloud-based API observability system built using Django REST Framework, Prometheus, and Grafana to monitor API request rates, latency, error rates, and system behavior in real time for performance analysis and troubleshooting.

## Tech Stack

- Backend: Django REST Framework
- Monitoring: Prometheus
- Visualization: Grafana
- Deployment: Render
- Load Testing: Apache JMeter

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/health/ | GET | Health check endpoint |
| /api/slow/ | GET | Simulates slow response (latency testing) |
| /api/error/ | GET | Simulates server error (500 response) |
| /api/random/ | GET | Random status simulation |
| /metrics | GET | Prometheus metrics endpoint (protected) |

## Observability Features

- Request rate tracking
- Response latency monitoring
- Error rate tracking (500, 429)
- Endpoint-wise traffic analysis
- Real-time dashboards using Grafana
- Alerting on latency and error thresholds

## Architecture

Client Requests
      ↓
Django REST API (Render)
      ↓
Prometheus Metrics Collection
      ↓
Grafana Dashboards & Alerts

## Screenshots

- Grafana dashboard (latency + errors)
<img width="1820" height="1499" alt="grafana_final_01" src="https://github.com/user-attachments/assets/72bcec74-59a6-4f93-9010-231064bbb27d" />

- Alert firing state
<img width="1455" height="779" alt="alert_grafana_01" src="https://github.com/user-attachments/assets/ab2329ca-cae4-4c4d-90d0-d86ef36fc45a" />

- Email Alerts
<img width="1494" height="93" alt="email_alert_grafana_01" src="https://github.com/user-attachments/assets/aba71fdc-113f-47e4-9d95-d7a714ea8c55" />

- API responses
  - /api/health/
    <img width="1617" height="552" alt="api_health_final_01" src="https://github.com/user-attachments/assets/f1ad8bf5-51b8-49f0-97ab-a663b14f068d" />

  - /api/error/
    <img width="1562" height="561" alt="api_error_final_01" src="https://github.com/user-attachments/assets/0d1c9de9-793d-4a79-bf2e-c3562695b6cd" />

  - /api/slow/
    <img width="1561" height="564" alt="api_slow_final_01" src="https://github.com/user-attachments/assets/50506290-c424-47fe-8b6a-70ef4b5e2da6" />

  - /api/random/
    <img width="1555" height="556" alt="api_random_final_01" src="https://github.com/user-attachments/assets/0de1da1d-df66-4bb3-b3ac-d4f646d572b8" />

  - Too many requests - Error 429
    <img width="1576" height="582" alt="error_429_final_01" src="https://github.com/user-attachments/assets/73ec78ff-1402-4fa5-9d70-cad7202ece3e" />
