package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
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