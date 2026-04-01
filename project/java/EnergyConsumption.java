package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A class for describing the energy consumption incurred by an AI model in
different stages of its lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnergyConsumption  {

  private List<EnergyConsumptionDescription> finetuningEnergyConsumption;
  private List<EnergyConsumptionDescription> inferenceEnergyConsumption;
  private List<EnergyConsumptionDescription> trainingEnergyConsumption;

}