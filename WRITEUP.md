# Write-up

### Analyze, choose, and justify the appropriate resource option for deploying the app.

* For **both** a VM or App Service solution for the CMS app:

| | VM | App Service |
|-|-|-|
| Cost | Typically, costs are higher due to the need to manage and pay for virtual machines, storage, and underlying network resources. | Generally offers lower costs as it is a managed service where Microsoft handles the infrastructure. |
| Scalability | Vertical and horizontal scaling possible. | Horizontal scaling supported, vertical scaling more limited |
| Availability | Need to configuration for high availability. | Provides built-in load balancing and auto-scaling features. |
| Workflow | Full control over OS, network, and applications.<br>Configuration and installation are required to perform CI/CD. | Limited control over underlying infrastructure, focused on application deployment.<br>Easier deployment through CI/CD pipelines. |

- I choose **App Service** to deploy my web application. Because:
    - App Service provides high availability and redundancy.
    - I don't want to worry about infrastructure, network, setup environment, etc.
    - Instead, I just focus on web application development.
    - I use SQL Database and Storage Account services for data and image storage needs. So Virtual Machine is not necessary.
    - Additionally, App Service enables quick and easy CI/CD.
    - Because the VM stays on even when not in use, the cost is higher, so I choose App Service to save costs.

### Assess app changes that would change your decision.
- If I need to micromanage, such as: OS, network, software, protocols, etc.
- If I am in the situation of transitioning  an application from an on-premises environment to the Cloud.