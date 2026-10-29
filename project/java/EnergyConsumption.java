package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A class for describing the energy consumption incurred by an AI model in different stages of its lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnergyConsumption  {

  private String type;
  private List<EnergyConsumptionDescription> finetuningEnergyConsumption;
  private List<EnergyConsumptionDescription> inferenceEnergyConsumption;
  private List<EnergyConsumptionDescription> trainingEnergyConsumption;


}