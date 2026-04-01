package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Provides a CVSS version 4 assessment for a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV4VulnAssessmentRelationship extends VulnAssessmentRelationship {

  private String severity;
  private String vectorString;
  private BigDecimal score;

}