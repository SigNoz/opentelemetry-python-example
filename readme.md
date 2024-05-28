# Guide on implementing OpenTelemetry in Python Applications

OpenTelemetry is an an open-source observability framework that aims to standardize the generation, collection, and management of telemetry data(Logs, metrics, and traces). It is incubated under Cloud Native Computing Foundation(Cloud Native Computing Foundation), the same foundation which incubated Kubernetes.

OpenTelemetry is quietly becoming the default standard for generating, transmitting and managing observability data and new-age companies are embracing it for future-proof instrumentation of their applications.

In this guide, you will learn how to implement OpenTelemetry in Python Applications. Following lessons cover everything you need to know about using OpenTelemetry to implement observability.

---

[Lesson 1: Setting up a basic Flask application](/lesson-1)   
In this tutorial, you will create a simple Flask to-do application with MongoDB.


[Lesson 2: Setting up SigNoz](/lesson-2)   
OpenTelemetry does not provide a storage and analytics layer. In this tutorial, you will set up SigNoz to send your OpenTelemetry data.

[Lesson 3-1: Auto-instrumentation with OpenTelemetry](/lesson-3-1)   
Set up automatic traces, metrics, and logs collection in the Flask application.

[Lesson 3-2: Manual instrumentation with OpenTelemetry](/lesson-3-2)   
Learn how to implement manual instrumentation with OpenTelemetry for more granular controls.

[Lesson 4: Create spans manually in your Python application](/lesson-4)   
Learn how to create manual spans and add metadata and attributes to them.

[Lesson 5: Create custom metrics with OpenTelemetry](/lesson-5)   
Create custom metrics like counter, gauge, histogram in your application.

[Lesson 6: Configure OpenTelemetry logging SDK in Python](/lesson-6)   
Learn how to configure OpenTelemetry logging SDK in Python.

[Lesson 7: Customize metrics streams produced by OpenTelemetry SDK using views](/lesson-7)   
In this tutorial, learn how to:
- how to configure to change the default aggregation using the name of the instrument
- how to have multiple exporter with different temporalities
- how to limit the number of attributes that are output for a metric
- how to drop a metric entirely

---

At the end of this tutorial series, you will be able to use OpenTelemetry effectively to monitor your Python application.

![application-metrics](https://github.com/ankit01-oss/opentelemetry-python-example/assets/83692067/bfaf97e5-bc61-4922-b3cc-eb9b336ca925)


