# Lesson 2: Setting up SigNoz

You need a backend to send data collected with OpenTelemetry. SigNoz is an OpenTelemetry-native observability backend that is best suited for visualizing OpenTelemetry data. It is a one-stop observability solution and provides logs, metrics, and traces under a single pane of glass.

With SigNoz, you can:

- Visualise Traces, Metrics, and Logs in a single pane of glass
- Monitor application metrics like p99 latency, error rates for your services, external API calls, and individual endpoints.
- Find the root cause of the problem by going to the exact traces which are causing the problem and see detailed flamegraphs of individual request traces.
- Run aggregates on trace data to get business-relevant metrics
- Filter and query logs, build dashboards and alerts based on attributes in logs
- Monitor infrastructure metrics such as CPU utilization or memory usage
- Record exceptions automatically in Python, Java, Ruby, and Javascript
- Easy to set alerts with DIY query builder

SigNoz is available both as an open-source software and as a cloud service.

## **SigNoz Cloud**

SigNoz cloud is the easiest way to run SigNoz. You can sign up [here](https://signoz.io/teams/) for a free account and get 30 days of unlimited access to all features.

In this tutorial series, we will be using SigNoz Cloud to visualize everything that we collect from our applications with OpenTelemetry.

After you sign up and verify your email, you will be provided with details of your SigNoz cloud instance. Once you set up your password and log in, you will be greeted with the following onboarding screen.


![SigNoz onboarding screen](../../static/images/onboarding-screen.png)

Since we will be following instructions from the tutorial, you can skip onboarding by clicking on the SigNoz logo.

You will see the below screen:

![Services tab in SigNoz shows the list of services being monitored](../../static/images/signoz-screen.png)

For sending data to SigNoz cloud, you will be needing details like ingestion key and region. You can find them under `Ingestion Settings` under `Settings`.

![Ingestion Settings](../../static/images/ingestion-settings.png)

## **Self-Host SigNoz**

You can also use the open-source version of SigNoz. Check out the [docs](https://signoz.io/docs/install/) for installing self-host SigNoz.

You can also check out our [GitHub repo](https://github.com/SigNoz/signoz).
