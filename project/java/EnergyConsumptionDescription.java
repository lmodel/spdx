package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  The class that helps note down the quantity of energy consumption and the unit
used for measurement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnergyConsumptionDescription  {

  private BigDecimal energyQuantity;
  private String energyUnit;

}