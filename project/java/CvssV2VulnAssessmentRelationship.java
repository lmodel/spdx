package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Provides a CVSS version 2.0 assessment for a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV2VulnAssessmentRelationship extends VulnAssessmentRelationship {

  private String vectorString;
  private BigDecimal score;

}