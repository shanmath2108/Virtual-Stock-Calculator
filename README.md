# Virtual-Stock-Calculator

## Description
This project is an object detection and inventory management system that uses YOLOv8 deep learning model to detect objects in a video stream. It uses this information to generate a report of the inventory present in the video stream. The inventory report is generated as a dictionary with item names and the corresponding prices.

## Features
1. Real-time Object Detection: YOLOv8 is employed to perform real-time, high-precision object detection. This capability enables businesses to continuously monitor the presence and location of inventory items within a given space.
2. Automated Inventory Calculation: The system computes and maintains the inventory levels of diverse items by continuously monitoring stock levels. This real-time approach eliminates the need for manual counts and significantly reduces the potential for human error.
3. Efficient Sales Tracking: Through real-time monitoring, the system enables automated sales tracking, providing businesses with immediate insights into their sales performance and helping to prevent stockouts or overstock situations.
4. User-friendly Interface: The Virtual Stock Calculator features an intuitive graphical interface that simplifies interactions for inventory managers and customers alike, enhancing the overall shopping experience.
5. Data Logging and Reporting: The system logs inventory changes and sales data, allowing businesses to generate detailed reports for data-driven decision-making and historical analysis.

## Requirements
The following dependencies are required to run the project:\
1. Python version above 3.6.0
2. Python modules:
  - OpenCV
  - Ultralytics
  - YOLOv8 (pre-trained model)
  - customtkinter
