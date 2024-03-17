//import org.apache.airflow.client.AirflowClient;
//import org.apache.airflow.models.DagRun;
//import org.apache.airflow.models.DagRunState;
//import org.apache.airflow.models.DagRunTrigger;
//import org.apache.airflow.models.DagRunTriggerType;
//
//public class AirflowExample {
//    public static void main(String[] args) {
//        // 初始化Airflow客户端
//        AirflowClient airflowClient = new AirflowClient.Builder()
//                .setAirflowUrl("http://your-airflow-webserver-url")
//                .setApiKey("your-api-key") // 如果需要认证
//                .build();
//
//        // 触发一个DAG
//        DagRunTrigger dagRunTrigger = new DagRunTrigger();
//        dagRunTrigger.setDagId("your-dag-id");
//        dagRunTrigger.setTriggerType(DagRunTriggerType.SCHEDULED);
//        DagRun dagRun = airflowClient.createDagRun(dagRunTrigger);
//
//        // 检查触发的DAG运行的状态
//        if (dagRun.getState() == DagRunState.RUNNING) {
//            System.out.println("DAG运行中。");
//        } else {
//            System.out.println("无法触发DAG运行。");
//        }
//    }
//}
