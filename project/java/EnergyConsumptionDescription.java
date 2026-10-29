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
  The class that helps note down the quantity of energy consumption and the unit used for measurement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnergyConsumptionDescription  {

  private String type;
  private BigDecimal energyQuantity;
  private String energyUnit;


}