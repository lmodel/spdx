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
  Provides an EPSS assessment for a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EpssVulnAssessmentRelationship extends VulnAssessmentRelationship {

  private BigDecimal percentile;
  private BigDecimal probability;


}